from threading import Thread
#python标准库队列
import queue
import time
#创建一个队列作为仓库
q=queue.Queue()
#生产者
class Producer(Thread):
    def run(self):
        count=0
        while True:
            if q.qsize()<50:
                for i in range(3):
                    count+=1
                    msg="产品%d"%count
                    q.put(msg)#将产品放入队列
            time.sleep(1)
class Customer(Thread):
    def run(self):
        while True:
            if q.qsize()>20:
                for i in range(2):
                    msg=q.get()#从仓库拿货
                    print("消费了%s"%msg,"还有%d"%q.qsize())
            time.sleep(1)
#创建两个生产
for i in range(2):
    p=Producer()
    p.start()
# 创建三个消费
for i in range(3):
    c=Customer()
    c.start()
