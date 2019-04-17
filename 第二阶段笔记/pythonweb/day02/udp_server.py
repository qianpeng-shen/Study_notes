# from socket import *
# import sys
# from time import ctime
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
# #绑定地址
# a.bind(ADDR)
# #收发消息
# while True:
#     data,adr=a.recvfrom(buffersize)
#     print('recv from %s:%s'%(adr,data.decode()))
#     a.sendto(('[%s] 接收到消息'%ctime()).encode(),adr)
# a.close()

from socket import *
import sys
from time import ctime
if len(sys.argv)<3:
    print("格式错误")
h=sys.argv[1]
p=int(sys.argv[2])
add=(h,p)
b=1024
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(add)
while True:
    data,adr=s.recvfrom(b)
    print("客户端为：",adr,"接收到的消息为：",data.decode())
    da=ctime()
    s.sendto(("%s为接收到的信息时间"%da).encode(),adr)
s.close()

