from socket import *
host=""
port=9999
#创建套接字
s=socket(AF_INET,SOCK_DGRAM)
#设置套接字可以接受广播
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#固定接受端的端口号
s.bind((host,port))
while True:
    try:
        message,addr=s.recvfrom(4096)
        print("从{}获取信息{}:".format(message,addr))
        s.sendto(b"I am here",addr)
    except (KeyboardInterrupt,SyntaxError):
        raise
    except Exception as e:
        print(e)
s.close()