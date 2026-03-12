import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',12345))
while True:
    mode=input("encrpt(e)/d=")
    key=input("enter key=")
    text=input("enter text=")
    if text=='bye':
        break
    s.send(f"{text}|{mode}|{key}".encode())
    result=s.recv(1024).decode()
    print("result==",result)
s.close()