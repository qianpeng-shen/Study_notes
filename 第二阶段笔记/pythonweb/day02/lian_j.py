# from socket import *
# from time import sleep
# a=socket()
# df=open("a",'rb')
# a.bind(('172.60.16.43',5263))
# a.listen(5)

# connfd,addr=a.accept()
# print(addr)
# while True:
#     data=df.read(128)
#     if not data:
#         sleep(0.5)
#         connfd.send(b'##')
#         break
#     connfd.send(data)
# df.close()
# connfd.close()
# a.close()

# from socket import * 
# from time import sleep
# s = socket() 
# s.bind(("127.0.0.1",8889))
# s.listen(5)
# c,addr = s.accept()
# print("Connect from ",addr)
# f = open('a','rb')
# while True:
#     data = f.read(1024)
#     if not data:
#         sleep(0.5)
#         c.send(b'#')
#         break
#     c.send(data)
# f.close()    
# c.close()
# s.close()
from socket import *
from time import *
s=socket()
s.bind(('172.60.16.43',4852))
s.listen(5)
df,addr=s.accept()
g=open('a','rb')
while True:
    data=g.read(128)

    if not data:
        sleep(0.5)
        df.send(b'##')
        break
    df.send(data)
d=df.recv(1024)
print(d.decode())
g.close()
df.close()
s.close()


