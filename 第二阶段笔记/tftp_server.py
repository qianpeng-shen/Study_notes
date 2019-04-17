from socket import *
import os,sys
import signal
import time
#确定文件库位置
FILE_PATH="/home/tarena/"
class TftpServer(object):
    def __init__(self,connfd):
        self.connfd=connfd
    def do_list(self):
        filelist=os.listdir(FILE_PATH)
        if not filelist:
            self.connfd.send(b'N')
            return 
        else:
            self.connfd.send(b"Y")
        time.sleep(0.1)
        files=''
        for filename in filelist:
            if filename[0] !='.' and os.path.isfile(FILE_PATH+filename):
                files=files+filename+'#'
        self.connfd.send(files.encode())
    def do_get(self,filename):
        try:
            f=open(FILE_PATH+filename,'rb')
        except:
            self.connfd.send(b'N')
            return
        self.connfd.send(b'Y')
        time.sleep(0.1)
        for line in f:
            self.connfd.send(line)
        f.close()
        time.sleep(0.1)
        self.connfd.send(b"##")
        print("发送文件成功")

    def do_put(self,filename):
        try:
            f=open(FILE_PATH+filename,"w")
        except:
            self.connfd.send(b"N")
            return
        self.connfd.send(b"Y")
        while True:
            data=self.connfd.recv(1024).decode()
            if data=="##":
                break
            f.write(data)
        f.close()
        print("接收文件成功")

def main():
    if len(sys.argv)<3:
        print("输入格式有错")
        sys.exit(1)
    host=sys.argv[1]
    port=int(sys.argv[2])
    ADDR=(host,port)
    BUFFRSIZE=1024
    #创建套接字
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            connfd,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit(0)
        except Exception:
            continue
        print("客户端登录",addr)
        pid=os.fork()
        if pid<0:
            print("创建子进程失败")
            continue
        elif pid==0:
            s.close()
            #创建客户端通信对象
            tftp=TftpServer(connfd)
            while True:
                #接收客户端请求类型
                data=connfd.recv(BUFFRSIZE).decode()
                if data[0]=='L':
                    tftp.do_list()
                elif data[0]=='G':
                    filename=data.split(' ')[-1]
                    tftp.do_get(filename)
                elif data[0]=="P":
                    filename=data.split(' ')[-1]
                    tftp.do_put(filename)
                elif data[0]=='Q':
                    print("客户端退出")
                    sys.exit(0)
        else:
            connfd.close()
            continue

if __name__=="__main__":
    main()
