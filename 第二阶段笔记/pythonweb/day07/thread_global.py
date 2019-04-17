from threading import Thread
from time import sleep
#全局变量a
#通过全局变量进行通信
a=1
def foo():
    global a
    #将全局变量a做修改
    a=1000
def bar():
    sleep(1)
    #此时全局变量a改变,变为100
    print("a=",a)#a=1000

t1=Thread(target=foo)
t2=Thread(target=bar)
t1.start()
t2.start()
t1.join()
t2.join()
print(a)
