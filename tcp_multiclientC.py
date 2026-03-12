import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break
def send():
    while True:
        message = input()
        client.send(message.encode())
threading.Thread(target=receive).start()
threading.Thread(target=send).start()