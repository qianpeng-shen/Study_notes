import threading 
from time import sleep
def music():
    while True:
        sleep(2)
        print("播放《活着》")
def sing():
    while True:
        sleep(2)
        print("kjkjk")
#创建线程和函数music关联
t=threading.Thread(target=music)
a=threading.Thread(target=sing)
#启动线程
t.start()
a.start()
while True:
    sleep(1.5)
    print("想听《花海》")
print("=======")
t.join()
a.join()
