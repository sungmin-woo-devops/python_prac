import socket

# 1st. internet socket or unix socket? internet socket
# 2nd. What kind of Protocol?
# 3rd. Which IP, port?

# Basic server script

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP
s.bind(('127.0.0.1', 55555))  # IP and port

# Listening: waits for possible connection
s.listen()

while True:
    # accept(): client tries to connect to the server
    client, address = s.accept()
    print("Connect to {}".format(address))
    client.send("You're connected!".encode())
    client.close()

# ------------------------------------------------------------
# How to send data over network
# How to exchange datas
# How to build a connection between server and clients

# Socket is just a endpoints of communication

# There're a lot of communication layers
# Sockets deals with TCP/IP, especially TCP and UDP.
# Higher layers - HTTP, FTP, ...

# ------------------------------------------------------------
# https://www.youtube.com/watch?v=iVZj9a4fog8
