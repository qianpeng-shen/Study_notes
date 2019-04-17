from multiprocessing import Process,Pipe
import os,time
# #创建一个双向管道
fd1,fd2=Pipe()
#如果参数为False　则fd1只能recv fd2只能send
# fd1,fd2=Pipe(False)

def fun(i):
    time.sleep(3)
    #发字符串到管道
    fd1.send('hello'+ str(i))
    print(os.getppid(),"----",os.getpid())


jobs=[]
for i in range(5):
    p=Process(target=fun,args=(i,))
    jobs.append(p)
    p.start()
for i in range(5):
    data=fd2.recv()
    print(data)
for i in jobs:
    i.join()