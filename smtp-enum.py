import socket
from urllib import response

# Pode ser alterado por uma lista
users = ["root", "test"]
for user in users:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("IP do servidor SMTP", 25))
    sock.recv(1024)
    sock.send("VRFY " + user + "\n")
    response = sock.recv(1024)
    sock.close()