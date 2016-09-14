import socket

# Allocate a new socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to google.ca
client.connect(('www.google.ca', 80))

http = "GET / HTTP/1.0\r\n\r\n"

client.sendall(http)

msg = ""
while True:
    part = client.recv(1024)
    if part:
       msg += part
    else:
       break

print msg
