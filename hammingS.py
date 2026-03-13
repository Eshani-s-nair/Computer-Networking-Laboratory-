import socket

def hdec(code):
    d=list(map(int,code))
    d7,d6,d5,p4,d3,p2,p1=d
    s1=d3^d5^d7^p1
    s2=d3^d6^d7^p2
    s4=d5^d6^d7^p4
    change=8-(s4*4+s2*2+s1)
    if change==0:
        return "No change"
    else:
        return f"change at pos:{change}"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',12345))
s.listen(1)
conn,addr=s.accept()
code=conn.recv(1024).decode()
conn.send(hdec(code).encode())