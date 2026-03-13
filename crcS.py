import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',12345))
s.listen(1)

def xor(a,b):
    res=""
    for i in range(1,len(b)):
        if a[i]==b[i]:
            res+='0'
        else:
            res+='1'
    return res

def mod2div(divisor,dividend):
    pick=len(divisor)
    temp=dividend[:pick]

    while pick<len(dividend):
        if temp[0]=='1':
            temp=xor(divisor,temp)+dividend[pick]
        else:
            temp=xor('0'*len(divisor),temp)+dividend[pick]
        pick+=1

    if temp[0]=='1':
        temp=xor(divisor,temp)
    else:
        temp=xor('0'*len(divisor),temp)

    return temp

key="1101"

conn,addr=s.accept()    
print("Connected to..",addr)
data=conn.recv(1024).decode()
print("Received data:", data)
remainder = mod2div(key,data)
if '1' in remainder:
    print("Error detected in received data")
else:
    print("No error detected")
conn.close()