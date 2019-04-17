"""
name:Levi
chatroom client
"""
from socket import *
import sys,os
import signal
#用子进程发送消息
def do_child(s,name,addr):
    while True:
        text=input("发消息(输入quit退出):")
        #用户退出
        if text=="quit":
            msg="Q "+name
            s.sendto(msg.endoce(),addr)
            #从子进程中杀掉父进程
            os.kill(os.getppid(),signal.SIGKILL)
            sys.exit("退出聊天室")
        #正常聊天
        else:
            msg="C %s %s"%(name,text)
            s.sendto(msg.encode(),addr)

#用父进程接收消息
def do_parent(s):
    while True:
        msg,addr=s.recvfrom(1024)
        print(msg.encode()+"\n发言(输入quit退出):",end="")
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return
    host=sys.argv[1]
    port=int(sys.argv[2])
    ADDR=(host,port)

    s=socket(AF_INET,SOCK_DGRAM,0)
    while True:
        name=input("请输入姓名:")
        msg='L ' +name
        s.sendto(msg.encode(),ADDR)
        data,addr=s.recvfrom(1024)
        if data.decode()=="OK":
            print("@进入聊天室@")
        else:
            print(data.decode())
        pid=os.fork()
        if pid<0:
            print("创建一级子进程失败")
        elif pid==0:
            do_child(s,name,ADDR)
        else:
            do_parent(s)

if __name__=="__main__":
    main()

# from socket imoprt *
# import sys,os
# import signal
# def do_child(s,name,addr):
#     while True:
#         tsxt=input("发言(输入quit退出)")
#         if text=="quit":
#             msg="Q"+name
#             s.sendto(msg.encode(),addr)
#             os.kill(os.getppid(),signal.SIGKILL)
#             sys.exit("退出聊天室")
#         else:
#             msg="C%s%s"%(name,text)
#             s.sendto(msg.encode(),addr)
# def do_parent(s):
#     while True:
#         msg.addr=s.recvfrom(1024)
#         print(msg.decode()+"\n发言(输入quit退出）：",end=" ")
# def fun():
#     if len(sys.argv)<3:
#         print("格式错误")
#     host=sys.argv[1]
#     port=int(sys.argv[2])
#     ADDR=(host,port)
#     s=socket(AF_INET,SOCK_DGRAM)
#     while True:
#         name=input("请输入姓名:")
#         msg="L "+name
#         s.sento(msg.encode(),ADDR)
#         data,addr=recvfrom(1024)
#         if data.decode()=='OK':
#             print("@进入聊天室@")
#             break
#         else:
#             print(data.decode())
#         pid=os.frok()
#         if pid<0:
#             print("创建子进程失败")
#         elif pid==0:
#             do_child(s,name,ADDR)
#         else:
#             do_parent(s)
# if __name__="__main__":
#     fun()
