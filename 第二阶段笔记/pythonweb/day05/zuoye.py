# import os
# from socket import *
# import multiprocessing as mp
# f=open('aa.py','rb')
# a=os.path.getsize('aa.py')
# n=a//2
# m=open("aab.txt","wb")
# def fun():
#     m.write(f.read(n))
#     m.close()
# p=mp.Process(target=fun())
# p.start()
# b=open("abc.txt","wb")
# f.seek(n)
# b.write(f.read())
# f.close()
# b.close()
import os
from socket import *
from multiprocessing import *
#在创建进程前获取文件对象，父子进程操作同一个文件流
#会造成操作混乱
# f=open('../day06/com.idddx.lwp.vivo.thebeauty_thumb.jpg','rb')
size=os.path.getsize('../day06/com.idddx.lwp.vivo.thebeauty_thumb.jpg')
def copy1():
    f=open('../day06/com.idddx.lwp.vivo.thebeauty_thumb.jpg','rb')
    n=size//2
    fw=open('copy1.jpg','wb')
    while True:
        if n<64:
            data=f.read(n)
            fw.write(data)
            break
        data = f.read(64)
        fw.write(data)
        n-=64
    fw.close()
    f.close()
def copy2():
    f=open('../day06/com.idddx.lwp.vivo.thebeauty_thumb.jpg','rb')
    fw=open('copy2.jpg','wb')
    f.seek(size//2,0)
    while True:
        data=f.read(64)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()
p1=Process(target=copy1())
p2=Process(target=copy2())
p1.start()
p2.start()
p1.join()
p2.join()
