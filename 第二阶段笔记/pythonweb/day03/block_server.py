# #非阻塞IO程序
# from socket import *
# from time import sleep,ctime
# a=socket(AF_INET,SOCK_STREAM,0)
# a.bind(('172.60.16.43',5264))
# a.listen(5)
#设置a是非阻塞状态
# a.setblocking(False)
# while True:
#     print("等待连接中......")
#     try:
#         connfd,addr=a.accept()
#     except BlockingIOError:
#         sleep(2)
#         print(ctime())
#         continue
#     print("如果爱,....",addr)
#     #recv变为非阻塞
#     #a.setblocking(False)
#     while True:
#         data=connfd.recv(5)
#         if not data:
#             break
#         print(data.decode())
#         connfd.send('有你，世界才美好'.encode())
#     connfd.close()
# a.close()
from socket import *
from time import sleep,ctime
import traceback
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('172.60.16.43',5214))
s.listen(10)
# s.setblocking(0)
s.settimeout(2)
while True:
    print("等待连接中......")
    try:
        connfd,addr=s.accept()
    except Exception:
        traceback.print_exc()
        continue
    print("连接的客户端地址为:",addr)
    while True:
        a=connfd.recv(1024)
        
        if not a:
            break
        print("接受ip地址为:",addr,"的内容为:",a.decode())
        connfd.send("天台".encode())
    connfd.close()
s.close()


