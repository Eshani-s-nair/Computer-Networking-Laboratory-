import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',12345))
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

def encrypt(data,key):
    l_key=len(key)
    append_data=data+'0'*(l_key-1)
    remainder=mod2div(key,append_data)
    codeword=data+remainder
    return codeword

def introduce_error(data):
    pos = int(input("Enter bit position to flip (starting from 0 )"))
    data = list(data)
    if data[pos] == '0':
      data[pos] = '1'
    else:
      data[pos] = '0'
    return ''.join(data)

key = "1101"
data = input("Enter data bits: ")
encoded_data = encrypt(data, key)
print("Encoded data (before error):", encoded_data)
choice = input("Do you want to introduce error? (y/n): ")
if choice.lower() == 'y':
 encoded_data = introduce_error(encoded_data)
 print("Data after introducing error:", encoded_data)
s.send(encoded_data.encode())
print("Data sent to server")
s.close()