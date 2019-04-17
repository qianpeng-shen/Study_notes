from socket import *

from threading import *
import os,sys
#处理具体的客户端请求
def handler(connfd):
    print("Got connection from ",connfd.getpeername())
    while True:
        data=connfd.recv(1024).decode()
        if not data:
            break
        connfd.send(b"receive your message")
    connfd.close()

HOST='172.60.16.43'
PORT=8814
#创建套接字
s=socket()
s.bind((HOST,PORT))
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(5)
#主线程循环接受客户端连接
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)
        continue
    t=Thread(target=handler,args=(c,))
    t.setDaemon(True)
    t.start()

s.close()
