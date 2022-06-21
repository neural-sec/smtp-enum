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
    if "252" in response:
        print(user + "-> Válido!")
    elif "550" in response:
        print(user + "-> Usuário não encontrado!")
    elif "503" in response:
        print("Servidor requer autenticação")
        break
    elif "500" in response:
        print("Comando VRFY não suportado pelo servidor")
        break
    else:
        print("Reposta do servidor: ", response)