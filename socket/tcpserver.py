
import socket

HOST = "127.0.0.1"
PORT = 65432

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and port
server.bind((HOST, PORT))

# Listen for client
server.listen()
print("Waiting for client...")

# Accept connection
conn, addr = server.accept()
print("Connected by", addr)

# Receive Celsius value
data = conn.recv(1024).decode()
celsius = float(data)

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Send result to client
result = str(fahrenheit)
conn.send(result.encode())

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

conn.close()
server.close()
