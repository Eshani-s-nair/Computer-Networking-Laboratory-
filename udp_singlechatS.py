import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))
while True:
    data,addr=server_socket.recvfrom(1024)
    if not data :
        break
    print(f"clent : {data.decode()}")
    reply=input("send message : ")
    server_socket.sendto(reply.encode(),addr)