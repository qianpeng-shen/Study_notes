from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print("s:",s.fileno())
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
print(s.type)
s.bind(('172.60.16.43',5264))
#获取绑定的地址
print(s.getsockname())
s.listen(5)
conn,addr=s.accept()
print(conn.getpeername())
while True:
    conn.recv(1024)