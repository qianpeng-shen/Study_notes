import threading
a=b=0
lock=threading.Lock()
def value():
    while True:
        lock.acquire()#加锁
        if a!=b:
            print("a=%d,b=%d"%(a,b))
        lock.release()#解锁

t=threading.Thread(target=value)
t.start()
while True:
    lock.acquire()
    a+=1
    b+=1
    lock.release()
t.join()
