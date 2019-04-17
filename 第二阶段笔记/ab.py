import sys 
from socket import *
from threading import Thread
ADDR=('0.0.0.0',8000)
static_root="./static"
handler_root="./handler"
class HTTPServer(object):
    def __init__(self,addr):
        self.socket=socket()
def main():
    if len(sys.argv)<3:
        sys.exit("输入格式错误，请输入一个模块和应用")
    sys.path.insert(0,handler_root)
    m=__import__(sys.argv[1])
    application=getattr(m,sys.argv[2])
    httpd=HTTPServer(ADDR)
    httpd.setApp(application)
    print("等待连接中")
    httpd.serveForever()
if __name__=="__main__":
    main()