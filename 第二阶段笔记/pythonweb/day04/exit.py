import os,sys

#结束进程
# os._exit(0)
try:
    sys.exit(1)
    print("我要执行")
except SystemExit as e:
    print(e)
#打印进程结束语
# sys.exit("结束了")
print("程序结束")