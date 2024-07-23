from flask import Flask, request, render_template_string
import os
import subprocess
import json

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
            save_data(mac, text)
            return 'Data submitted successfully!'
    return render_template_string(html_template)

@app.route('/get_mac')
def get_mac():
    client_ip = request.remote_addr
    mac = get_mac_address(client_ip)
    mac = ":".join(mac.split("-"))
    return mac

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
