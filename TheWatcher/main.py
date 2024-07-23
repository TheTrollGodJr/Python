import discord
from dotenv import load_dotenv
import os
from discord.ext import commands, tasks
from scapy.all import ARP, Ether, srp
import socket
from flask import Flask, request, render_template_string
import subprocess
import json
import threading
import asyncio

'''

    MUST HAVE NPCAP DOWNLOADED:
    https://npcap.com/#download

'''

def get_local_ip():
    """Get the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external server; doesn't actually send data
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

def scan_network(ip_range):
    """Scan the network for devices and return their IP and MAC addresses."""
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered_list:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def getMacs():
    local_ip = get_local_ip()
    ip_parts = local_ip.split('.')
    network_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"

    # Scan the network
    devices = scan_network(network_range)
    macs = []
    for device in devices:
        macs.append(device['mac'])
    return macs

def getPeople():
    mac = getMacs()

    with open("TheWatcher/data.json","r") as f:
        data = json.load(f)

    people = []
    for items in mac:
        try: people.append(data[items])
        except: pass
    
    return people

def discordBot():
    load_dotenv(dotenv_path="C:/Users/thetr/Documents/Python/token/token.env")
    token = os.getenv('watcherBot')

    intents = discord.Intents.default()
    intents.message_content = True 
    #bot = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix="!", intents=intents)
    #tree = discord.app_commands.CommandTree(bot)

    @bot.event
    async def on_ready():
        #await tree.sync(guild=discord.Object(id=1249089474244116542))
        print(f"{bot.user} is connected")
        eventLoop.start()
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @tasks.loop(seconds=60)
    async def eventLoop():
        global newMember
        global people
        #global peopleOld
        print("looped")

        if len(newMember) > 0:
            channel = bot.get_channel(1249089474244116545)
            await channel.send(f"### *{newMember}* has joined The House")
            newMember = ""
        
        #peopleOld = people
        people = getPeople()
        print(people)

    @bot.tree.command(name="help")
    async def help(interaction: discord.Interaction):
        await interaction.response.send_message("## Help Commands:\n> **/help** - Returns a list off all bot commands\n> **/people** - Returns a list of all people at the house\n> **/exit** - Turns the bot off", ephemeral=True)
    
    @bot.tree.command(name="people")
    async def people(interaction: discord.Interaction):
        global people
        out = ""
        for items in people:
            out += f"> {items}\n"

        if len(out) > 0:
            await interaction.response.send_message(f"## These people are currently at the house:\n{out}", ephemeral=True)
        else:
            await interaction.response.send_message("## Nobody is home right now")
    
    @bot.tree.command(name="exit")
    async def exit(interaction: discord.Interaction):
        sender = interaction.user.id
        if sender == 413501255533461505:
            #shutdownFlask()
            await interaction.response.send_message("Shutting Down Bot")
            await bot.close()
        else:
            await interaction.response.send_message("You do not have permission to use this command", ephemeral=True)

    bot.run(token)


def website():
    app = Flask(__name__)

    # HTML template for the webpage linking to external CSS
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MAC Address and Text Submission</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            label {
                display: block;
                margin: 10px 0 5px;
            }
            input[type="text"] {
                width: 96%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                width: 100%;
                padding: 10px;
                background-color: #007BFF;
                border: none;
                color: white;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .redirect-button {
                width: 100%;
                padding: 8px;
                background-color: #28a745;
                border: none;
                color: white;
                border-radius: 4px;
                cursor: pointer;
                margin-top: 10px;
            }
            .redirect-button:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Enter Your Name</h1>
            <form id="mac-form" action="/" method="post">
                <input type="text" id="text" name="text" required>
                <input type="hidden" id="mac" name="mac">
                <button type="submit">Submit</button>
            </form>
            <button class="redirect-button" onclick="redirect()">Discord Server link</button>
            <script>
                document.getElementById('mac-form').addEventListener('submit', async function(event) {
                    event.preventDefault();
                    const mac = await fetch('/get_mac').then(response => response.text());
                    document.getElementById('mac').value = mac;
                    // Perform the form submission manually
                    const formData = new FormData(event.target);
                    const response = await fetch(event.target.action, {
                        method: 'POST',
                        body: formData
                    });
                    if (response.ok) {
                        // Redirect to a different link after successful submission
                        window.location.href = 'https://discord.gg/CvYAxmnt87';
                    } else {
                        alert('There was an issue with your submission.');
                    }
                });

                function redirect() {
                    window.location.href = 'https://discord.gg/CvYAxmnt87';
                }
            </script>
        </div>
    </body>
    </html>
    '''

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            text = request.form['text']
            mac = request.form['mac']
            if mac != "" and not("." in mac):
                global newMember
                newMember = text
                save_data(mac, text)
                return 'Data submitted successfully!'
        return render_template_string(html_template)

    @app.route('/get_mac')
    def get_mac():
        client_ip = request.remote_addr
        mac = get_mac_address(client_ip)
        return mac
    
    def shutdown():
        pass

    def get_mac_address(ip):
        try:
            # Run arp -a to get the ARP table
            arp_output = subprocess.check_output(['arp', '-a'], encoding='utf-8')
            for line in arp_output.splitlines():
                if ip in line:
                    # Extract MAC address from the ARP table entry
                    return line.split()[1]
        except Exception as e:
            print(f"Error getting MAC address: {e}")
        return ""

    def save_data(mac, text):
        data = {}
        # Check if the data.json file exists and read its content
        if os.path.exists('TheWatcher/data.json'):
            with open('TheWatcher/data.json', 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    data = {}
                    print(e)

        # Append the new data
        data[mac] = text

        # Write the updated data back to the file
        with open('TheWatcher/data.json', 'w') as f:
            json.dump(data, f, indent=4)

    app.run(host='0.0.0.0', port=5000, debug=True)

def shutdownFlask():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with Werkzeug Server')
    func()

if __name__ == "__main__":
    #website()
    newMember = ""
    people = []

    discordThread = threading.Thread(target=discordBot)
    discordThread.start()

    #website()