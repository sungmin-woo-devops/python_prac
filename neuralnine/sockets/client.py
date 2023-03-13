import socket

# get Public IP on myip.is : 118.36.208.176
HOST = '192.168.0.17'
PORT = 9998

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))
