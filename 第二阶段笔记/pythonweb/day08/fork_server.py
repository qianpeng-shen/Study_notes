from socket import *
import os,sys
import signal
#创建套接字
host='172.60.16.54'
poet=8945
def client_handler(c):
    try:
        print("子进程接收客户端的请求",c.getpeername())
        while True:
            data=c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(b"receive your message")
    except (KeyboardInterrupt,SystemExit):
        raise
    except Exception as e:
        print(e)
    c.close()
    sys.exit(0)


s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((host,poet))
s.listen(1)
print("父进程%d 等待客户端连接"%os.getpid())
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        raise
    except Exception as e :
        print(e)
        continue
    #为新的客户端创建新的进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    pid=os.fork()
    if pid<0:
        print("创建子进程失败")
        c.close()
        continue
    elif pid==0:
        s.close()
        #处理客户端请求
        client_handler(c)

    else:
        c.close()
        continue

