from socket import *
import os,sys
import signal
import time
FILE_PATH＝"/home/tarena/"



def main():
    if len(sys.argv)<3:
        print("输入的格式错误,请重新输入")
        sys.exit(1)
    host=sys.argv[1]
    port=int(sys.argv[2])
    ADDR=(host,port)
    buffresize=1024
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            connfd.addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit(0)
        except Exception:
            continue
        print("客户端登录")
        pid=os.fork()
