import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
client.connect((host, port))

print("Connected to server.")
while True:
    mode = input("Choose mode - Compress(c) / Decompress(d): ").lower()
    if mode not in ["c", "d"]:
        print("Invalid mode. Try again.")
        continue
    text = input("Enter text or code: ")
    message = f"{mode}|{text}"
    client.send(message.encode())
    result = client.recv(4096).decode()
    print("Server:", result)