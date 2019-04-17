import os,sys
from time import sleep

pid=os.fork()
if pid<0:
    print("Create process failed")
elif pid==0:
    print("Child process...")
    sleep(2)
    sys.exit(2)
else:
    #设置为非阻塞状态，循环处理查看子进程状态
    while True:
        try:
            p,status=os.waitpid(-1,os.WNOHANG)
            sleep(0.5)
            # p,status=os.waitpid(-1,0)
            print("parent process")
            print(p,status)
        except ChildProcessError:
            print("程序完成")
            break
    while True:
        pass