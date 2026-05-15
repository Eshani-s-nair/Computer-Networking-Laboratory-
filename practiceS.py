import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',12345))
s.listen(1)

def compress(text):
    dictionary={chr(i):i for i in range(256)}
    w="" 
    dic_size=256
    res=[]
    for c in text:
        wc=w+c
        if wc in dictionary:
            w=wc
        else:
            res.append(dictionary[w])
            dictionary[wc]=dic_size
            dic_size+=1
            w=c
    if w:
        res.append(dictionary[w])
    return " ".join(map(str,res))

def decompress(text):
    code=list(map(int,text.split()))
    dictionary={i:chr(i) for i in range(256)}
    dict_size=256
    w=chr(code[0])
    res=[w]
    for c in code[1:]:
        if c in dictionary:
            entry=dictionary[c]
        else:
            entry=w+w[0]
        res.append(entry)
        dictionary[dict_size]=w+entry[0]
        dict_size+=1
        w=entry
    return "".join(res)

client, addr = s.accept()
print("Client connected:", addr)
while True:
    data = client.recv(4096).decode()
    mode, text = data.split("|", 1)
    if mode == "c":
        result = compress(text)
    elif mode == "d":
        result = decompress(text)
    else:
        result = "Invalid mode"
    client.send(result.encode())

    

