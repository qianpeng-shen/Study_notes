#!/usr/bin/env python3
#coding=utf-8
''' 
name:levi
date:5-30
phone:110
This is dict projecct for aid 1803
MOLULES python3.5 mysql pymysql
'''
from socket import *
import pymysql
import sys,os
import signal
import time
#服务器:注册　登录　查词　历史记录　
class TftpServer(object):
    def __init__(self,connfd,db,cur):
        self.connfd=connfd
        self.db=db
        self.cur=cur
    def do_child(self,data):
        if data=="登录":
            self.do_login()
        elif data=="注册":
            self.do_register()
        elif data=="退出":
            print("客户端退出")
            sys.exit(0)
    def do_login(self):
        data=self.connfd.recv(1024).encode()
        ab='select * from user where name=%s'%data
        dat=self.cur.execute(ab)
        if dat=="True":
            self.s.send(b'Y')
            self.do_chuli()
        else:
            self.send(b'N')
    def do_register(self):
        data=self.connfd.recv(1024).encode()
        ab='select %s from user'%data
        dat=self.cur.execute(ab)
        if dat=="True":
            self.s.send(b'Y')
            dab="insert into "
        else:
            self.send(b'N') 
    def do_chuli(self):
        pass
def mian():
    if len(sys.argv)<3:
        sys.exit("输入格式错误，请重新输入")
    db=pymysql.connect('localhost','root','123456','dict',charset='utf8')
    cur=db.cursor()
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
    BUFFRSIZE=1024
    ADDR=(HOST,PORT)
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
            tftp=TftpServer(connfd,db,cur)
            while True:
                #接收客户端请求类型
                data=connfd.recv(BUFFRSIZE).decode()
                tftp.do_child(data) 
        else:
            connfd.close()
            continue
if __name__=="__main__":
    mian()