import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=('127.0.0.1',12345)

name=input("enter name")
s.sendto(name.encode(),host)
message,_=s.recvfrom(1024)
data=message.decode()
print(data)

def receive():
    while True:
        message,_=s.recvfrom(1024)
        data=message.decode()
        print(data)
        if data=="quiz ended":
            break
        reply=input("enter the answer : ")
        s.sendto(reply.encode(),host)
        message,_=s.recvfrom(1024)
        data=message.decode()
        print(data)
threading.Thread(target=receive).start()