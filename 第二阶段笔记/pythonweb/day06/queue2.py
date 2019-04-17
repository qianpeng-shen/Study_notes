from multiprocessing import Process,Queue
import time
#创建一个消息队列
q=Queue()

def fun():
    time.sleep(1)
    q.put("我是神")
def fun1():
    time.sleep(2)
    print("取消息",q.get())

p1=Process(target=fun)
p2=Process(target=fun1)
p1.start()
p2.start()
p1.join()
p2.join()
