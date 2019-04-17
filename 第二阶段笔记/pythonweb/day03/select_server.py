from socket import *
from select import *
import sys
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('172.60.16.43',5264))
s.listen(10)
#将关注的IO放入rlist
rlist=[s]
wlist=[]
xlist=[]
while True:
    
    rs,ws,xs=select(rlist,wlist,xlist)

    for r in rs:
        if r is s:
            connfd,addr=r.accept()
            print("Connect from",addr)
            #将新的套接字加入到关注列表
            rlist.append(connfd)
        else:
            try:
                data=r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                print("Receive from:",r.getpeername(),":",data.decode())
                #想发消息可以放到关注列表
                wlist.append(r)
            except Exception:
                pass
    for w in ws:
        w.send("天地悠悠，一壶浊酒".encode())
        wlist.remove(w)
    for x in xs:
        if x is s:
            s.close()
            sys.exit(1)
# from socket import *
# from select import *
# import sys
# s=socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('172.60.16.43',5214))
# s.listen(10)
# rlist=[s]
# wlist=[]
# xlist=[s]
# while True:
#     rs,ws,xs=select(rlist,wlist,xlist)
#     for r in rs:
#         if r is s:
#             coonfd,addr=r.accept()
#             print("客户端地址",addr)
#             rlist.append(coonfd)
#         else:
#             try:
#                 data=r.recv(1024)
#                 if not data:
#                     rlist.remove(r)
#                     r.close()
#                 print("接收到的消息是：",data.decode())
#                 wlist.append(r)
#             except Exception:
#                 pass
#     for w in ws:
#         w.send("你们就是渣".encode())
#         wlist.remove(w)
#     for x in xs:
#         if w is s:
#             s.close()
#             sys.exit(1)



