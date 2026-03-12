import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',12345))
while True:
    mode=input("enter mode(e/d): ")
    text=input("enter text: ")
    key=input("enter key: ")
    data=f"{mode},{text},{key}"
    s.send(data.encode())
    result=s.recv(1024).decode()
    print(f"{mode.title()} {text} -> {result}")