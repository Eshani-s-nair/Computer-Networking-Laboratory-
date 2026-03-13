import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

server.bind((host, port))
server.listen(1)

def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    w = ""
    dict_size = 256
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return " ".join(map(str, result))


def lzw_decompress(code_str):
    codes = list(map(int, code_str.split()))
    dictionary = {i: chr(i) for i in range(256)}
    w = chr(codes[0])
    result = [w]
    dict_size = 256
    for k in codes[1:]:
        if k in dictionary:
            entry = dictionary[k]
        else:
            entry = w + w[0]
        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return "".join(result)


print(f"Server running on {host}:{port}")
client, addr = server.accept()
print("Client connected:", addr)
while True:
    data = client.recv(4096).decode()
    mode, text = data.split("|", 1)
    if mode == "c":
        result = lzw_compress(text)
    elif mode == "d":
        result = lzw_decompress(text)
    else:
        result = "Invalid mode"
    client.send(result.encode())