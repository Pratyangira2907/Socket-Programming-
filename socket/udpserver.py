
import socket

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = "127.0.0.1"
PORT = 12345

# Bind IP and port
server.bind((HOST, PORT))

print("Waiting for client...")

# Receive Celsius value
data, addr = server.recvfrom(1024)

celsius = float(data.decode())

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Send result to client
result = str(fahrenheit)
server.sendto(result.encode(), addr)

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

server.close()
