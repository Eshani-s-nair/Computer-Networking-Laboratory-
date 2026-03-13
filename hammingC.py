import socket

def henc(data):
    d=list(map(int,data))
    d7,d6,d5,d3=d
    p1=d3^d5^d7
    p2=d3^d6^d7
    p4=d5^d6^d7
    return f"{d7}{d6}{d5}{p4}{d3}{p2}{p1}"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',12345))

data=henc(input("enter data"))
flip=input("flip?(y/n) ")
if flip=='y':
    pos=int(input("position?"))
    pos=pos-1
    if data[pos]=='0':
        code=data[0:pos]+'1'+data[pos+1:]
    else:
        code=data[0:pos]+'0'+data[pos+1:]
else:
    code=data
    print(code)
s.send(code.encode())
result=s.recv(1024).decode()
print(result)
