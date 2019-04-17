# from socket import *
# import sys
# #从命令行传入ip和端口
# #格式 python3 udpp_server.py 172.0.0.1 8888
# if len(sys.argv)<3:
#     print("""argv is error!!!
#         input as
#         python3 udpp_server.py 172.0.0.1 8888""")
# host=sys.argv[1]
# port=int(sys.argv[2])
# ADDR=(host,port)
# buffersize=1024
# #创建数据报套接字
# a=socket(AF_INET,SOCK_DGRAM)
# while True:
#     data=input("消息>>")
#     #回车退出
#     if not data:
#         break
#     a.sendto(data.encode(),ADDR)
#     data,addr=a.recvfrom(buffersize)
#     print("从服务器收到",data.decode())
# a.close()
from socket import *
import sys
if len(sys.argv)<3:
    print("格式错误")
h=sys.argv[1]
p=int(sys.argv[2])
addr=(h,p)
b=1024
s=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("请输入》》》")
    if not data:
        break
    s.sendto(data.encode(),addr)
    data,adr=s.recvfrom(b)
    print("从服务器收到",data.decode())
s.close()