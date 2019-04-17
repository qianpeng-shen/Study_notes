#客户端\
from socket import *
from sys,os
import time
import pymysql
import signal
def main():
    if len(sys.argv)<3:
        print("输入格式错误，请重新输入")
    HOST=sys.argv[1]
    POST=int(sys.argv[2])
    s=socket()
    s.connect((HOST,POST))
    
