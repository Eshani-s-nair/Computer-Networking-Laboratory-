def gentxt(text):
    text=text.upper().replace('J','I').replace(' ','')
    res=''
    i=0
    while(i<len(text)):
        res+=text[i]
        if i+1<len(text) and text[i]==text[i+1]:
            res+='X'
        i+=1
    if(len(res)%2!=0):
        res+='X'
    return res
def genkeysq(key):
    key=key.upper().replace('J','I')
    key_sq=[]
    for ch in key+'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if ch not in key_sq:
            key_sq.append(ch)
    return key_sq
def encrypt(a,b,keysq):
    r1,c1=divmod(keysq.index(a),5)
    r2,c2=divmod(keysq.index(b),5)
    if r1==r2:
        return keysq[r1*5+(c1+1)%5]+keysq[r2*5+(c2+1)%5]
    elif c1==c2:
        return keysq[((r1+1)%5)*5+c1]+keysq[((r2+1)%5)*5+c2]
    else:
        return keysq[r1*5+c2]+keysq[r2*5+c1]
    
def decrypt(a,b,keysq):
    r1,c1=divmod(keysq.index(a),5)
    r2,c2=divmod(keysq.index(b),5)
    if r1==r2:
        return keysq[r1*5+(c1-1)%5]+keysq[r2*5+(c2-1)%5]
    elif c1==c2:
        return keysq[((r1-1)%5)*5+c1]+keysq[((r2-1)%5)*5+c2]
    else:
        return keysq[r1*5+c2]+keysq[r2*5+c1]

def playfire(text,mode,key):
    text=gentxt(text)
    keysq=genkeysq(key)
    res=''
    for i in range(0,len(text),2):
        a=text[i]
        b=text[i+1]
        if mode=='e':
            res+=encrypt(a,b,keysq)
        else:
            res+=decrypt(a,b,keysq)
    return res

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',12345))
s.listen(1)
conn,addr=s.accept()
print("Connected to..",addr)
while True:
    data=conn.recv(1024).decode()
    text,mode,key=data.split('|')
    res=playfire(text,mode,key)
    conn.send(res.encode())
conn.close()
s.close()