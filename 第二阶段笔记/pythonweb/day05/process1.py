import multiprocessing as mp
import os
import time
a=1
def fun():
    global a
    a=1000
    print(os.getppid(),"----",os.getpid())
    print("吃早饭")
    time.sleep(1)
    print("吃午饭")
    time.sleep(2)
    print("吃晚饭")
    time.sleep(3)
def fun2():
    print(os.getppid(),"----",os.getpid())
    print("睡午觉")
    time.sleep(2)
    time.sleep(3)
    print("睡觉")
    print(a)
def fun3():
    print(os.getppid(),"----",os.getpid())
    print("打豆豆")
    time.sleep(2)
    print("打小豆豆")
    time.sleep(2)

#创建三个新的进程，关联上面三个事件，达到运行的目的
#生成三个进程对象分别表示这三个进程

p1=mp.Process(target=fun)
p2=mp.Process(target=fun2)
p3=mp.Process(target=fun3)
#通过生成的进程对象启动子进程
#子进程有父进程的代码段　只不过只执行对应的函数

p1.start()
p2.start()
p3.start()
print("Parent PID",os.getpid())
#阻塞等待回收进程
p1.join()
p2.join()
p3.join()
print("+++++++")
# fun()
# fun2()
# fun3()