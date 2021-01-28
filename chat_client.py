import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip=input("Enter Server IP : ")
sport=int(input("Enter Server Port : "))

def sender():
    while True:
        data=input("Enter Messege : ")
        mydata=data.encode()
        s.sendto(mydata,(sip,sport))
        x=s.recvfrom(100)
        data=x[0].decode()
        if(data=='exit the chat' ):
            print("Exit from chat")
            break
        print(data)


sender()
