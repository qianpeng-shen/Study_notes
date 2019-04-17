from multiprocessing import *
from time import sleep

def worker(sec,msg):

    for i in range(3):
        sleep(sec)
        print("worker message:",msg)
#位置传参
# p=Process(target=worker,args=(2,"hello"))
#字典传参
# p=Process(target=worker,kwargs={'sec':2,'msg':'hello'})
p=Process(target=worker,args=(2,),kwargs={'msg':'hello'})

p.start()
print("p.name:",p.name)
#P所代表的子进程的PID号
print("p.pid:",p.pid)
print("p.alive:",p.is_alive())
p.join()

print("+++++")
