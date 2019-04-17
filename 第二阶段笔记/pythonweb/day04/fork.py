#os 为系统相关模块，不同操作系统使用情况不同
import os
# from test import *
print("准备创建进程")
a=1

pid=os.fork()
if pid<0:
    print("创建进程失败")

elif pid==0:
    print("创建了一个新的进程")
    # fun1()
else:
    print("这是原有的进程")
    # fun2()

print("进程进行完毕")