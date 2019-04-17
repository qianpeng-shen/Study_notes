# from socket import  *
# #1创建流式套接字
# sockfd=socket(AF_INET,SOCK_STREAM,0)
# #sockfd是返回值

# #2绑定IP端口
# sockfd.bind(('127.0.0.1',9651))

# #3设置为监听套接字，创建监听队列
# sockfd.listen(5)
# while True:
#     print("waiting for connect...")
#     #4等待客户端连接
#     connfd,addr=sockfd.accept()
#     print("connect from",addr)
#     while True:
#         #5收发消息
#         data=connfd.recv(1024)
#         if not data:
#             break

#         print(data.decode())
#         connfd.send('爱的供养'.encode())
#     #6关闭套接字
#     connfd.close()
# sockfd.close()

from socket import *
a=socket(AF_INET,SOCK_STREAM,0)
a.bind(('172.60.16.64',8882))
a.listen(5)
while True:
    print("等待连接中......")
    connfd,addr=a.accept()
    print("如果爱,....",addr)
    while True:
        data=connfd.recv(5)
        # print("-------",data)
        if not data:
            break
        print(data.decode())
        connfd.send('有你，世界才美好'.encode())
    connfd.close()
a.close()

# from socket import *
# s=socket()
# s.bind(('172.60.16.43',5254))
# s.listen(5)
# print("等待收信息中")
# while True:
#     c,addr=s.accept()
#     while True:
#         g=c.recv(1024)
#         print("收到的信息是：",g.decode())
#         hg=input("请输入信息:>>>>")
#         c.send(hg.encode())
#     c.close()
# s.close()
