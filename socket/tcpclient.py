
import socket

HOST = "127.0.0.1"
PORT = 65432

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Get Celsius temperature
celsius = input("Enter temperature in Celsius: ")

# Send Celsius value
client.send(celsius.encode())

# Receive Fahrenheit result
data = client.recv(1024).decode()

print("Temperature in Fahrenheit:", data)

client.close()
