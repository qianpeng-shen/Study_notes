import threading
from time import sleep
s=None
#创建线程对象
e=threading.Event()
def fun1():
    print("和fun2进行沟通")
    global s
    s="天街小雨润如酥"
def fun2():
    print("等待口令")
    sleep(2)
    if s == "天街小雨润如酥":
        print("fun2收到",s)
    else:
        print("口令有误")
    e.set()
def fun3():
    print("改掉口令")
    sleep(1)
    e.wait()#阻塞
    global s
    s="不下了"#想要将全局变量s改为"不下了",导致fun2接受的消息将发生改变
t1=threading.Thread(name='fun1',taregt=fun1)
t2=threading.Thread(name='fun2',taregt=fun2)
t3=threading.Thread(name='fun3',taregt=fun3)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()