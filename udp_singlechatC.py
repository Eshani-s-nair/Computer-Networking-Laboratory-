import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=('127.0.0.1',12345)
while True:
    message=input("enter the message : ")
    if message.lower()=="exit":
        break
    client_socket.sendto(message.encode(),host)
    data,addr=client_socket.recvfrom(1024)
    print(f'server : {data.decode()}')
client_socket.close()

