import os
from time import *

pid=os.fork()
if pid<0:
    print("死")
elif pid==0:
    print("子进程")
    print("getpid:",os.getpid())#子进程自己获取自己的pid
    print("getppid:",os.getppid())#子进程获取父进程的pid
else:
    sleep(1)
    print("父进程")
    print("pid",pid)#父进程fork返回值就是子进程PID
    print("getpid",os.getpid())#父进程获取自己的pid