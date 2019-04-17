import gevent
from gevent import monkey
#在导入socket前执行，改变socket的阻塞形态
monkey.patch_all()
from socket import *
from time import ctime
def server(port):
    s=socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)
    while True:
        c,addr=s.accept()
        pprint("Connect from",addr)
        gevent.spawn(handler,c)
#处理客户端事件
def handler(c):
    while True:
        data=c.recv(1024).decode()
        print("recv",data)
        if not data:
            break
        c.send(ctime().encode())
    c.close()
if __name__=="__main__":
    server(8080)
