# from socket import *
# a=socket()
# a.connect(('172.60.16.43',5263))
# df=open("jio.txt",'w')
# while True:
#     data=a.recv(1024).decode()
#     if data == "##":
#         break
#     df.write(data)
# df.close()
# a.close()

# from socket import *

# s = socket()

# s.connect(("127.0.0.1",8889))

# f = open('jio.txt','w')

# while True:
#     data = s.recv(1024).decode()
#     if data == '#':
#         break
#     f.write(data)

# f.close()
# s.close()
from socket import *
s=socket()
s.connect(("172.60.16.43",4852))
f=open('jio.txt','w')
while True:
    data=s.recv(4096).decode()
    if data=='##':
        break
    f.write(data)
s.send("接受完毕".encode())
f.close()
s.close()


