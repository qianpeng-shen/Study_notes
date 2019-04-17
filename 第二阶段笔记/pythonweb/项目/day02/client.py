from socket import *
import sys
#客户端:图形界面打印　提出请求　接受反馈　反馈展示
class Thtpclient(object):
    def __init__(self,s):
        self.s=s
    def do_loging(self,data):
        self.s.send(data.encode())
        while True:
            a=input("请输入用户名")
            self.s.send(a.encode())
            b=input("请输入密码")
            self.s.send(b.encode())
            ab=self.s.recv(1024).decode()
            if ab=="Y":
                do_chuli()
            else:
                continue

    def do_register(self,data):
        self.s.send(data).encode()
        while True:
            a=input("请输入用户名")
            self.s.send(a.encode())
            b=input("请输入密码")
            self.s.send(b.encode())
            ab=self.s.recv(1024).decode()
            if ab=="Y":
                do_chuli()
            else:
                continue
    def do_chuli(self):
        print("=====请选择=====")
        print("=====query=====")
        print("====register====")
        a=input("请输入您的选项")
        self.s.send(a.endoce())
        if a=="query":
            self.do_query()
        elif a=="register":
            self.do_register()
    def do_query(self):
        pass
    def do_register(self):
        pass
def main():
    if len(sys.argv)<3:
        sys.exit("输入格式错误，请重新输入")
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
    ADDR=(HOST,PORT)
    s=socket()
    BUFFRSIZE=1024
    s.connect(ADDR)
    tftp=Thtpclient(s)
    while True:
        print("======选择选项======")
        print("========登录========")
        print("========注册========")
        print("========退出========")
        print("====================")
        data=input("请输入命令>>>")
        if data=="登录":
            tftp.do_loging(data)
        elif data=="注册":
            tftp.do_register(data)
if __name__=="__main__":
    main()