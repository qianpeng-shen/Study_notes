from multiprocessing import Queue
from time import sleep
#创建队列
q=Queue(3)

q.put(1)
print(q.full())
q.put(2)
q.put(3)
print(q.full())
#超时时间为3
# q.put(4,True,3)
print("取出值为",q.get())
print("队列中有%d条消息"%q.qsize())
sleep(0.1)
print("队列是否为空:",q.empty())
q.close()#关闭队列