import socket

# host = socket.gethostbyname(socket.gethostname())
# print(host)
# HOST = host

HOST = '192.168.0.17'
# HOST = 'localhost' or '127.0.0.1'
PORT = 9998

# socket 타입 정의: socket인데 무슨 socket?
# TCP(SOCK_STRAM) or UDP(SOCK_DGRAM)?
# socket below is only for connecting communication
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    # waits connection to come in 
    communication_socket, address = server.accept()
    print(f"Connecte to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")


    
