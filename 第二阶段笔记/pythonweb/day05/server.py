'''
name : Levi
chatroom server
'''
from socket import *
import sys,os
def do_login(s,user,name,addr):
    if (name in user) or name=="管理员":
    # for i in user:
    #     if i==name or name=="管理员":
            # s.sendto("该用户已存在，请重新输入".encode(),addr)
            # return
        s.sendto("该用户已存在，请重新输入".encode(),addr)
        return
    s.sendto(b'OK',addr)
    msg="\n欢迎 %s 进入聊天室"%name
    #通知所有人
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户插入字典
    user[name]=addr
    return
def do_chat(s,user,cmd):
    msg="\n%-4s: %s"%(cmd[1]," ".join(cmd[2:]))
    #发送给所有人，除了自己
    for i in user:
        if i!=cmd[1]:
            s.sendto(msg.encode(),user[i])
    return
def do_quit(s,user,name):
    del user[name]
    msg="\n"+name+"离开了聊天室"
    for i in user:
        s.sendto(msg.encode(),user[i])
    return
#子进程处理客户请求
def do_child(s):
    #字典用来存储用户信息
    user={}
    #循环接受请求
    while True:
        msg,addr=s.recvfrom(1024)
        msg=msg.decode()
        cmd=msg.split(' ')
        #根据不同请求做不同事情
        if cmd[0]=="L":
            do_login(s,user,cmd[1],addr)
        elif cmd[0]=="C":
            do_chat(s,user,cmd)
        elif msg=="Q":
            do_quit(s,user,cmd[1])
        else:
            s.sendto("请求错误".encode(),addr)
#发送管理员消息
def do_parent(s,addr):
    while True:
        msg=input("管理员消息:")
        msg="C 管理员"+msg
        s.sendto(msg.encode(),addr)
    s.close()
    sys.exit(0)
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return
    host=sys.argv[1]
    port=int(sys.argv[2])
    ADDR=(host,port)
    #使用数据报套接字
    s=socket(AF_INET,SOCK_DGRAM,0)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    pid1=os.fork()
    if pid1<0:
        print("创建一级子进程失败")
    elif pid1==0:
        pid2=os.fork()
        if pid2<0:
            print("创建二级子进程失败")
        elif pid2==0:
            do_child(s)
        else:
            os._exit(0)
    else:
        os.wait()
        do_parent(s,ADDR)
if __name__=="__main__":
    main()

# from socket import *
# import os,sys
# def do_login(s,user,name,addr):
#     if (name in user) or name=="管理员":
#         s.send("该用户已存在，请重新输入".encode(),addr)
#         return
#     s.sendto(b"OK",addr)
#     msg="\n欢迎%s进入聊天室"%name
#     for i in user:
#         s.sendto(msg.encode(),user[i])
#     user[name]=addr
#     return
# def do_chat(s,user,cmd):
#     msg="\n%-4s"%(cmd[1]," ".join(cmd[2:]))
#     for i in user:
#         if i != cmd[1]:
#             s.send(msg.encode(),user[i])
#         return
# def do_quit(s,user,name):
#     del user[name]
#     msg='\n'+name+"离开聊天室"
#     for i in user:
#         s.sendto(msg.encode(),user[i])
#     return

# def fun1(s):
#     user={}
#     while True:
#         connfd,addr=recvfrom(1024)
#         connfd=connfd.decode()
#         cmd=connfd.split(" ")
#         if cmd[0]=="L":
#             do_login(s,user,cmd[1],addr)
#         elif cmd[0]=="C":
#             do_chat(s,user,cmd)
#         elif cmd[0]=="Q":
#             do_quit(s,user,cmd[1])
#         else:
#             s.send("请求错误".encode(),addr)
# def fun2(s.addr):
#     while True:
#         msg=input("管理员消息:")
#         msg="C管理员"+msg
#         s.sendto(msg.encode(),addr)
#         s.close()
#         sys.exit(0)
# def fun():
#     if len(sys.argv)<3:
#         print("格式错误")
#         return
#     host=sys.argv[1]
#     post=int(sys.argv[2])
#     ADDR=(host,post)
#     s=socket(AF_INET,SOCK_DGRAM,0)
#     s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#     s.bind(ADDR)
#     pid=os.fork()
#     if pid<0:
#         print("创建子进程失败")
#     elif pid==0:
#         pid1=os.fork()
#         if pid1<0:
#             print("创建二级子进程失败")
#         elif pid==0:
#             fun1(s)
#         else:
#             os._exit(0)
#     else:
#         os.wait()
#         fun2()

# if __name__="__main__":
#     fun()


