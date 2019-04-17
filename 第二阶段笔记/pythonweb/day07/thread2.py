#线程属性
from threading import Thread,currentThread
from time import sleep
def fun(sec):
    print("线程属性测试")
    sleep(sec)
    print("%s线程结束"%currentThread().getName())

thread=[]
for i in range(3):
    t=Thread(name='tedu'+str(i),target=fun,args=(5,))
    t.start()
    thread.append(t)

for i in thread:
    print("thread name :",i.name)
    print("alive :",i.is_alive())
    i.join()