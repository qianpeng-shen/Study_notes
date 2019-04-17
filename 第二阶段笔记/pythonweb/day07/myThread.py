from threading import Thread
from time import ctime,sleep
#编写自己的线程类
class Mythread(Thread):
    def __init__(self,func,args,name='Tedu'):
        #如果没有执行父类__init__方法
        # Thread.__init__(self)
        super().__init__()
        self.func=func
        self.args=args
        self.name=name
    #调用start会自动运行
    #重写run方法
    def run(self):
        player()     args=('baby.mp3',3)
        self.func(*args)
def player(file,sec):
    for i in range(2):
        print("playing %s :%s"%(file,ctime()))
        sleep(sec)
t=Mythread(player,('baby.mp3',3))
t.start()
t.join()
