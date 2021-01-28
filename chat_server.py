import socket
import threading as th
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("10.0.0.32",2345))

def chfun(x):
    data= x[0].decode()
    clip=x[1][0]
    clport=x[1][1]
    print(clip+ " : " + data)
    reply=input("What reply you want to send to client {} ".format(clip))
    rep=reply.encode()
    s.sendto(rep, (clip,clport))
    if reply=='exit the chat':
        print("Exiting the system")
        s.close()
        os._exit(os.EX_OK)

def server():
    print("Server is started, waiting for Client to join the Chat App")
    while True:
        x=s.recvfrom(30)
        t=th.Thread(target=chfun,args=(x,))
        t.start()

server()

