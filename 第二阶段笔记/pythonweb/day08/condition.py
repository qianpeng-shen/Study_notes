import threading
import time
import datetime

num=0

#条件变量
con=threading.Condition()
class Gov(threading.Thread):
    def run(self):
        global num
        con.acquire()
        while True:
            print("开始拉升股市")
            num+=1
            print("拉升了%d个点"%num)
            time.sleep(2)
            if num==5:
                print("暂时安全")
                con.notify()
                print("不操作")
                con.wait()
        con.release()
class Consumers(threading.Thread):
    def run(self):
        global num
        con.acquire()
        while True:
            if num>0:
                print("开始打压股市")
                num-=1
                print("下降了%d个点"%num)
                time.sleep(2)
                if num==0:
                    print("天台在哪，我要自杀")
                    con.notify()
                    print("不能再下降了")
                    con.wait()
        con.release()
t1=Gov()
t2=Consumers()
t1.start()
t2.start()