from  multiprocessing import Process,Lock
import sys
from time import sleep
def worker1():
    # with lock:
    lock.acquire()#上锁
    for i in range(5):
        sleep(1)
        sys.stdout.write("worker1 输出\n")
    lock.release()#解锁
def worker2():
    #with方式上锁
    with lock:
        for i in range(5):
            sleep(1)
            sys.stdout.write("worker2 输出\n")


#创建一个lock对象
lock=Lock()
#标准输入
sys.stdin
#标准输出
sys.stdout
w1=Process(target=worker1)
w2=Process(target=worker2)
w1.start()
w2.start()
w1.join()
w2.join()