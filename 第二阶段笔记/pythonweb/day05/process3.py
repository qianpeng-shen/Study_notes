import multiprocessing as mp
import os
import time

def fun():
    print(os.getppid(),"----",os.getpid())
    print("吃早饭")
    time.sleep(1)
    print("吃午饭")
    time.sleep(2)
    print("吃晚饭")
    time.sleep(3)
def fun2():
    print(os.getppid(),"----",os.getpid())
    print("睡午觉")
    time.sleep(2)
    time.sleep(3)
    print("睡觉")
def fun3():
    print(os.getppid(),"----",os.getpid())
    print("打豆豆")
    time.sleep(2)
    print("打小豆豆")
    time.sleep(2)
things=[fun,fun2,fun3]
process=[]
for i in things:
    p=mp.Process(target=i)
    p.daemon=True
    process.append(p)
    p.start()
print("+++父进程++++++")
# for i in process:
#     i.join()

# p1=mp.Process(target=fun)
# p2=mp.Process(target=fun2)
# p3=mp.Process(target=fun3)

# p1.start()
# p2.start()
# p3.start()

# p1.join()
# p2.join()
# p3.join()
