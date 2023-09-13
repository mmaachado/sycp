import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 4466))
    client.send(b"MENSAGEM\n")
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except Exception as error:
    print("Um erro ocorreu.")
    print(error)