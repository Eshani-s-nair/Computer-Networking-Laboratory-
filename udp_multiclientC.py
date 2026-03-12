import socket
import threading
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 12345)

name = input("Enter your name: ")
client_socket.sendto(name.encode(), server_addr)
def receive():
    while True:
        try:
            data, addr = client_socket.recvfrom(1024)
            print(data.decode())
        except:
            break
threading.Thread(target=receive, daemon=True).start()
while True:
    message = input()
    client_socket.sendto(message.encode(), server_addr)

    if message.lower() == "exit":
        break
client_socket.close()