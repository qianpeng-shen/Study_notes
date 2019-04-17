import os,sys
from time import sleep

pid=os.fork()

if pid<0:
    print("Cueate process failed")
elif pid==0:
    print("Child process....",os.getpid())
    sleep(2)
    sys.exit(5)
else:
    p,status=os.wait() 
    print(p,status)
    print(os.WEXITSTATUS(status))#此方法得到退出状态  5
    while True:
        pass