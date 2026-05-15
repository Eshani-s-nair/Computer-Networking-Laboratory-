import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',12345))
questions={
    1:["1+1","2"],
    2:["2+2","4"]
}

msg,addr=s.recvfrom(1024)
data=msg.decode()
print("client sent a message")
s.sendto(f"hello welcome {data} , lets start the quiz".encode(),addr)
i=1

while i<=len(questions):

    s.sendto(questions[i][0].encode(),addr)
    answer,addr=s.recvfrom(1024)
    ans=answer.decode()
    print(f"client  to question {questions[i][0]} : {ans}")

    if ans ==questions[i][1]:
        s.sendto("correct answer".encode(),addr)
    else:
        s.sendto("wrong answer".encode(),addr)
    i+=1
s.sendto("quiz ended".encode(),addr)
s.close()
