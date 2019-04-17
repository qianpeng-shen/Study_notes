from socket import *
import os,sys
import signal
import time
class Tftpclient(object):
    def __init__(self,s):
        self.s=s
    #服务器回复Y/N
    def do_list(self):
        self.s.send(b'L')
        data=self.s.recv(1024).decode()
        if data=="Y":
            data=self.s.recv(4096).decode()
            files=data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完毕")
        else:
            print("请求文件列表失败")
    #下载   
    def do_get(self,filename):
        self.s.send(('G '+filename).encode())
        data=self.s.recv(1024).decode()
        if data=='Y':
            f=open(filename,'w')
            while True:
                data=self.s.recv(1024).decode()
                if data=="##": 
                    break
                f.write(data)
            f.close()
            print("%s下载文件成功"%filename)
        else:
            print("输入文件不存在，请重新输入")
    def do_put(self,filename):
        try:
            f=open(filename,'rb')
        except:
            print("上传文件不存在")
            return
        self.s.send(b"P "+filename.encode())
        data=self.s.recv(1024).decode()
        if data=='Y':
            while True:
                data=f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)
            f.close()
            print("上传 %s 完成"%filename)
        else:
            print("上传文件失败")
    def do_quit(self):
        self.s.send(b'Q')
        self.s.close()
        sys.exit(0)
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
    s.connect(ADDR)
    #创建客户端请求对象
    tftp=Tftpclient(s)
    while True:
        print("=========命令选项==========")
        print("*********list*************")
        print("********get file**********")
        print("********put file**********")
        print("*********quit*************")
        print("==========================")
        data=input("输入命令>>>>")
        if data.strip()=="list":
            tftp.do_list()
        elif data[:3]=="get":
            filename=data.split(' ')[-1]
            tftp.do_get(filename)
        elif data[:3]=="put":
            filename=data.split(' ')[-1]
            tftp.do_put(filename)
        elif data.strip()=="quit":
            tftp.do_quit()
        else:
            print("请输入正确的命令!!!")



if __name__=="__main__":
    main()
