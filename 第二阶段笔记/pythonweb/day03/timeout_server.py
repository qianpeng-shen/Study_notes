
from socket import *
from time import sleep,ctime
import traceback

a=socket(AF_INET,SOCK_STREAM,0)
a.bind(('172.60.16.43',5264))
a.listen(5)
#设置a超时检测
a.settimeout(5)
while True:
    print("等待连接中......")
    try:
        connfd,addr=a.accept()
    except Exception:
        traceback.print_exc()
        continue
    print("如果爱,....",addr)
    #recv设置超时检测
    #connfd.settimeout(3)
    while True:
        data=connfd.recv(5)
        if not data:
            break
        print(data.decode())
        connfd.send('有你，世界才美好'.encode())
    connfd.close()
a.close()