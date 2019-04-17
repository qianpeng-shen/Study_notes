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

HOST='0.0.0.0'
PORT=8000
ADDR=(HOST,PORT)
DICT_TEXT='./zidian.py'
def main():
    #数据库库连接
    db=pymysql.connect('localhost','root','123456','dict')
    #创建套接字
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #忽略子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr=s.accept()
            print("等待客户端连接")
        except KeyboardInterrupt:
            os._exit(0)#处理　终端按ctrl+c异常
        except:
            continue#处理其他异常
        #创建子进程
        pid=os.fork()
        if pid<0:
            print("子进程创建失败")
            c.close()
        elif pid==0:
            s.close()
            do_child(c,db)
        else:
            c.close()
            continue
def do_child(c,db):
    #循环接受请求
    while True:
        data=c.recv(128).decode()
        if data[0] =='R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)
        elif data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'Q':
            do_query(c,db,data)
        elif data[0] == 'H':
            do_history(c,db,data)
def do_register(c,db,data):
    print("执行注册操作")
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    sql="select * from user where name='%s'" % name
    cursor.execute(sql)
    r=cursor.fetchone()
    print(r)
    if r != None:
        c.send(b'EXISTS')
        return
    sql="insert into user(name,passwd) values('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b'FALL')
        db.rollback()
        return
    else:
        print("注册成功")
def do_login(c,db,data):
    print("登录成功")
    l=data.split(' ')
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    try:
        sql="select * from  user where name='%s' and passwd='%s'"%(name,passwd)
        cursor.execute(sql)
        r = cursor.fetchone()
    except:
        print("我错了")
    if r == None :
        c.send(b'FALL')
    else:
        c.send(b'OK')
def do_query(c,db,data):
    print("查询动作")
    l=data.split(' ')
    name=l[1]
    word=l[2]
    cursor=db.cursor()
    def insert_history():
        tm=time.ctime()
        sql="insert into hist (name,word time) values('%s','%s','%s')"%(name,word,tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            return
    try:
        f=open(DICT_TEXT,'rb')
    except :
        c.send(b'FALL')
        return
    while True:
        line=f.readline().decode()
        tmp=line.split(' ')
        if tmp[0] > word:
            c.send(b"FALL")
            f.close()
            break
        if tmp[0]==word:
            c.send(b'OK')
            time.sleep(0.1)
            c.send(line.encode())
            insert_history()
            break
    f.close()
def do_history(c,db,data):
    print('历史记录')
    name=data.split(' ')[1]
    cursor=db.cursor()
    try:
        sql="select * from hist where name='%s'"%name
        cursor.execute(sql)
        r=cursor.fetchall()
        if not r :
            c.send(b'FALL')
        else:
            c.send(b'OK')
    except:
        pass
    for i in r:
        time.sleep(0.1)
        msg="%s %s %s"%(i[1],i[2],i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b"##")
if __name__=="__main__":
    main()
