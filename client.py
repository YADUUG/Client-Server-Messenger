import socket
import threading

def receive_messages():
    while True:
        message = client.recv(1024).decode()
        print("\n", message)

def send_message():
    while True:
        message = input()
        client.send(message.encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
