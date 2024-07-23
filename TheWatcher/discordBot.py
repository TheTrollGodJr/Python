import discord
from dotenv import load_dotenv
import os
from discord.ext import commands, tasks
from scapy.all import ARP, Ether, srp
import socket
import json

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
    print(mac, "\n")

    with open("TheWatcher/data.json","r") as f:
        data = json.load(f)
        print(data)

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
        global people

        mac = getMacs()
        print(mac, "\n")

        with open("TheWatcher/data.json","r") as f:
            data = json.load(f)
            print(data)

        people = []
        for items in mac:
            try: people.append(data[items])
            except: pass
        
        print(people)
    

    @bot.tree.command(name="help")
    async def help(interaction: discord.Interaction):
        await interaction.response.send_message("## Help Commands:\n> **/help** - Returns a list off all bot commands\n> **/people** - Returns a list of all people at the house\n> **/exit** - Turns the bot off", ephemeral=True)
    
    @bot.tree.command(name="people")
    async def people(interaction: discord.Interaction):
        global people
        out = ""
        for items in people:
            out += f"### - {items}\n"

        if len(out) > 0:
            await interaction.response.send_message(f"## These people are currently at the house:\n{out}", ephemeral=True)
        else:
            await interaction.response.send_message("## Nobody is home right now", ephemeral=True)
    
    @bot.tree.command(name="exit")
    async def exit(interaction: discord.Interaction):
        sender = interaction.user.id
        if sender == 413501255533461505:
            #shutdownFlask()
            await interaction.response.send_message("Shutting Down Bot", ephemeral=True)
            await bot.close()
        else:
            await interaction.response.send_message("You do not have permission to use this command", ephemeral=True)

    bot.run(token)

if __name__ == "__main__":
    people = []
    discordBot()