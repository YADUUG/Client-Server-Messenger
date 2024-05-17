import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print("Received message:", message)
        broadcast(message)

def broadcast(message):
    for client in clients:
        client.send(message.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(5)

clients = []

print("Server is listening...")

while True:
    client_socket, addr = server.accept()
    print("Connected with", addr)
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
