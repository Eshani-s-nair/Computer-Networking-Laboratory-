import socket
import threading
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen()
clients = []
def broadcast(message, sender_conn):
    for conn, name in clients:
        if conn != sender_conn:
            try:
                conn.sendall(message.encode())
            except:
                conn.close()
                clients.remove((conn, name))

def handle_client(conn, name):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            if message.lower() == "exit":
                broadcast(f"{name} left the chat", conn)
                break
            print(f"{name}: {message}")
            broadcast(f"{name}: {message}", conn)
        except:
            break
    conn.close()
    clients.remove((conn, name))

while True:
    conn, addr = server_socket.accept()
    conn.send("Enter your name: ".encode())
    name = conn.recv(1024).decode().strip()
    print(f"{name} connected from {addr}")
    clients.append((conn, name))
    conn.send("Connected to chat server.\n".encode())
    broadcast(f"{name} joined the chat!", conn)
    thread = threading.Thread(target=handle_client, args=(conn, name))
    thread.start()