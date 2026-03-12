import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(1)
conn,addr=server_socket.accept()
print(f'connection estabished with {addr}')
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    print(f'client : {data}')
    reply=input("server : ")
    conn.send(reply.encode())
