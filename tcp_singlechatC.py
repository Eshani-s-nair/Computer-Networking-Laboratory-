import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))
print("connected successfully ")
while True:
    message=input("enter message : ")
    if message.lower()=="exit":
        break
    client_socket.send(message.encode())
    data=client_socket.recv(1024).decode()
    print(f'server : {data}')
client_socket.close()
