from multiprocessing import Process
import os,time


def fun():
    print("getpid:",os.getpid())
p=Process(target=fun)
p.start()
print(p.pid)
p.join()