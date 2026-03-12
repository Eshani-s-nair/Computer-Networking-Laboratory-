import socket
def railEncrypt(text,key):
    rail=['' for _ in range(key)]
    row,dir=0,1
    for ch in text:
        rail[row]+=ch
        if row==0: dir=1
        elif row==key-1: dir=-1
        row+=dir
    return ''.join(rail)
    
def railDecrypt(cipher,key):
    rail=[['\n' for _ in range(len(cipher))] for _ in range(key)]
    row,dir=0,1
    for i in range(len(cipher)):
        rail[row][i]='*'
        if row==0: dir=1
        elif row==key-1: dir=-1
        row+=dir

    index=0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c]=='*' and index<len(cipher):
                rail[r][c]=cipher[index]
                index+=1
    
    result=[]
    row,dir=0,1
    for i in range(len(cipher)):
        result.append(rail[row][i])
        if row==0: dir=1
        elif row==key-1: dir=-1
        row+=dir

    return ''.join(result)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',12345))
s.listen(1)

conn,addr=s.accept()
while True:
    data=conn.recv(1024).decode()
    mode,text,key=data.split(',')
    if text=='bye':
        break
    key=int(key)
    if mode=='e':
        res=railEncrypt(text,key)
    else:
        res=railDecrypt(text,key)
    conn.send(res.encode())
conn.close()




        

