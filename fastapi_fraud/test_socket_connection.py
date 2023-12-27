import socket
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(("hostname", port))
except socket.gaierror as e:
    print("Connection error:", e)
finally:
    s.close()
