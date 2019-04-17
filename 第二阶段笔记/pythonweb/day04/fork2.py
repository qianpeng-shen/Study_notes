import os
from time import sleep

pid=os.fork()

if pid<0:
    print("Cueate process failed")
elif pid==0:
    #父进程已经退出，打印的将是新的父进程pid
    sleep(1)
    # print("my parent pid:",os.getppid())
    print("child pid",os.getpid())
else:
    #子进程退出，父进程不退出
    sleep(1)
    while True:
        pass
    # print("Parent pid:",os.getpid())