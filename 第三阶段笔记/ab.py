#服务器
from socket import *
from sys,os
import time
import pymysql
import signal

HOST="0.0.0.0"
PORT=8000
ADDR=(HOST,PORT)
def main():
    s=socket()
    db=pymysql('hocalhost','root','123456','dict')
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(10)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr=s.accept()
            print("等待客户端连接")
        except KeyboardInterrupt:
            o._exit()
        except:
            continue
        pid=os.fork()
        if pid<0:
            print("子进程创建失败")
            c.close()
        elif pid == 0:
            s.close()
            do_child(c,db)
        else:
            c.close()
            continue
