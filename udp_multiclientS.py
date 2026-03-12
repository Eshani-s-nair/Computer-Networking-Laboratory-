import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))

clients = {} 
print("UDP Chat Server Started")
while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode().strip()
    if addr not in clients:
        name = message
        clients[addr] = name
        print(f"{name} connected from {addr}")
        server_socket.sendto("Connected successfully".encode(), addr)
        continue
    name = clients[addr]
    if message.lower() == "exit":
        print(f"{name} left the chat")
        del clients[addr]
        continue
    print(f"{name}: {message}")
    for client_addr in clients:
        if client_addr != addr:
            server_socket.sendto(f"{name}: {message}".encode(), client_addr)