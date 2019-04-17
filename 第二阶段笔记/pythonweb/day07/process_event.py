from multiprocessing import Event,Process
from time import sleep
def wait_event():
    print("prooo1我也想操作临界区，要阻塞等待主进程")
    e.wait()
    print("主进程操作完成，该我了",e.is_set())
def wait_event_timeout():
    print("proooo2我也想操作临界区，要阻塞等待主进程")
    e.wait(2)
    print("我不等了，先执行别的",e.is_set())

e=Event()

p1=Process(name='block',target=wait_event)
p2=Process(name='non-block',target=wait_event_timeout)
p1.start()
p2.start()
e.wait(2)
print("假设正在忙碌的操作临界资源")
sleep(3)
e.set()
print("主进程操作完了，开放临界区")
p1.join()
p2.join()
