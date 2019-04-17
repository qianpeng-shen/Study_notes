from scoket import *
import os,sys
import signal
import time
class Tftpclient(self):
    def __init__(self,s):
        sefl.s=s
    def do_list(self):
        self.s.send

def main():
    if len(sys.argv)<3:
        print("输入格式错误")
        sys.exit(1)
    host=sys.argv[1]
    port=int(sys.argv[2])
    ADDR=(host,port)
    buffrsize=1024
    s=sockert()
    s.connect(ADDR)
    tftp=Tftpclient(s)
    while True:
        print("==========命令选项===========")
        print("************list************")
        print("**********get file**********")
        print("**********put file**********")
        print("************quit************")
        print("============================")
        data=input("输入命令>>>>")
        if data.strip()=="list":
            tftp.do_list()
        elif data[:3]=="get":
            filename=data.split(" ")[-1]
            tftp.do_get(filename)
        elif data[:3]=="put":
            filename=data.split(" ")[-1]
            tftp.do_put(filename)
        elif data.strip()=="quit":
            tftp.do_quit()
        else:
            print("输入内容不存在，请重新输入")
if __name__=="__main__":
    main()