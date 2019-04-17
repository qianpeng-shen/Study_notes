# 作业 : 
# 信号通信 
# 司机和售票员的故事
# 1. 创建父子进程，分别表示司机和售票员
# 2. 当售票员捕捉到 SIGINT信号时 给司机发送 SIGUSER1信号， 
# 此时司机打印 “老司机开车了”
#    当售票员捕捉到  SIGQUIT时 给司机发送 SIGUSER2信号，
# 此时司机打印“系好安全带，车速有点快”
#    当司机捕捉到 SIGTSTP时，发送SIGUSER1给售票员，售票员打印 
# “到站了，请下车”
# 3. 到站后 售票员先下车（子进程退出）,然后司机下车
# from signal import *
# from  time import sleep
# from multiprocessing import Process,Queue
# import os
# from signal import *
# def saler(sig,frame):
#     if sig==SIGINT:
#         os.kill(os.getppid(),SIGUSR1)
#     elif sig==SIGQUIT:
#         os.kill(os.getppid(),SIGUSR2)
#     elif sig==SIGUSR1:
#         print("到站了，请下车") 
#         os._exit(0)      
# def fun1(sig,frame):
#     if sig==SIGUSR1:
#         print("老司机开车了")
#     elif sig==SIGUSR2:
#         print("系好安全带，车速有点快")
#     elif sig==SIGTSTP:
#         os.kill(p.pid,SIGUSR1)
# #售票员
# def handler():
#     signal(SIGINT,saler)
#     signal(SIGQUIT,saler)
#     signal(SIGUSR1,saler)
#     signal(SIGTSTP,SIG_IGN)
#     while True:
#         sleep(2)
#         print("开车")
# s=Process(target=handler)
# s.start()
# signal(SIGUSR1,fun1)
# signal(SIGUSR2,fun1)
# signal(SIGTSTP,fun1)
# signal(SIGINT,SIG_IGN)
# signal(SIGQUIT,SIG_IGN)
# s.join()
# 作业 : 
# 信号通信 
# 司机和售票员的故事
# 1. 创建父子进程，分别表示司机和售票员
# 2. 当售票员捕捉到 SIGINT信号时 给司机发送 SIGUSER1信号， 
# 此时司机打印 “老司机开车了”
#    当售票员捕捉到  SIGQUIT时 给司机发送 SIGUSER2信号，
# 此时司机打印“系好安全带，车速有点快”
#    当司机捕捉到 SIGTSTP时，发送SIGUSER1给售票员，售票员打印 
# “到站了，请下车”
# 3. 到站后 售票员先下车（子进程退出）,然后司机下车
from multiprocessing import *
import os,time
from signal import *
def fun1(sig,frame):
    if sig==SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig==SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig==SIGUSR1:
        print("到站了，请下车")
        os._exit(0)
def fun2(sig,format):
    if sig==SIGUSR1:
        print("老司机开车了")
    elif sig==SIGUSR2:
        print("系好安全带")
    elif sig==SIGTSTP:
        os.kill(p.pid,SIGUSR1)
#售货员
def fun():
    signal(SIGINT,fun1)
    signal(SIGQUIT,fun1)
    signal(SIGUSR1,fun1)
    signal(SIGTSTP,SIG_IGN)
    while True:
        time.sleep(1)
        print("带你飞")
p=Process(target=fun)
p.start()
signal(SIGUSR1,fun2)
signal(SIGUSR2,fun2)
signal(SIGTSTP,fun2)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)
p.join()