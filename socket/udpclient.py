
import socket

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = "127.0.0.1"
PORT = 12345

# Get Celsius temperature
celsius = input("Enter temperature in Celsius: ")

# Send Celsius value to server
client.sendto(celsius.encode(), (HOST, PORT))

# Receive Fahrenheit result
data, addr = client.recvfrom(1024)

print("Temperature in Fahrenheit:", data.decode())

client.close()
