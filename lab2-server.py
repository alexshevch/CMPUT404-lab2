import socket

# Allocate a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Magic line we add to be able to reuse ports
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Listen on port 8000
server.bind(('0.0.0.0', 8000))
server.listen(1)

print "Waiting for connecions..."
client, address = server.accept()
print "Connected!"
print address

# client is going to be curl, web browser, etc.
outgoing = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
outgoing.connect(('www.google.ca', 80))
outgoing.setblocking(0)
client.setblocking(0)
while True:
    try:
        part = client.recv(1024)

    except socket.error,exception:
        if exception.errno == 11:
            part = None
        else:
            raise
    if part:
        outgoing.sendall(part)
        print "<" + part
    try:
        part = outgoing.recv(1024)
    except socket.error,exception:
        if exception.errno == 11:
            part = None
        else:
            raise
    if part:
        print "> " + part
        client.sendall(part)
