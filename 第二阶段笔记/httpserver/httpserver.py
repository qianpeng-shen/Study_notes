import sys 
from socket import *
from threading import Thread
#全局变量
ADDR=('0.0.0.0',8000)
static_root='./static'
hanler_root='./hanler'
class HTTPServer(object):
    def __init__(self,addr):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)

    def serveForever(self):
        while True:
            self.connfd,self.clientAddr=self.sockfd.accept()
            clientThread=Thread(target=self.handleRequest)
            clientThread.start()
    def setApp(self,application):
        self.application=application
    def handleRequest(self):
        self.recvData=self.connfd.recv(2048)
        requestHeaders=self.recvData.splitlines()
        for lien in requestHeaders:
            print(lien)
        getRequest=str(requestHeaders[0]).split(' ')[1]
        if getRequest[-3:] !=".py":
            if getRequest=="/":
                getFilename=static_root+"/index.html"
            else:
                getFilename=static_root+getRequest
            try:
                f=open(getFilename)
            except:
                responseHeaders="HTTP/1.1 404 not find\r\n"
                responseHeaders+="\r\n"
                reponseBody="===sorry,file not find==="
            else:
                responseHeaders="HTTP/1.1 200 OK\r\n"
                responseHeaders+="\r\n"
                reponseBody=f.read()
            finally:
                response=responseHeaders+reponseBody
                self.connfd.send(response.encode())
        else:
            env={}
            bodyContent=self.application(env,self.startResponse)
            response="HTTP/1.1 {}\r\n".format(self.header_set[0])
            for header in self.header_set[1:]:
                response+="{0}:{1}\r\n".format(*header)
            response+="\r\n"
            response+=bodyContent
            self.connfd.send(response.encode())
        self.connfd.close()
    def startResponse(self,status,response_headlers):
        serverHeaers=[('Date','2018-5-21'),('Server',"HTTPServer 1.0")]
        self.header_set=[status,response_headlers+serverHeaers]
def main():
    if len(sys.argv)<3:
        sys.exit("请选择一个模块个应用")
    sys.path.insert(0,hanler_root)
    m=__import__(sys.argv[1])
    application=getattr(m,sys.argv[2])
    httpd=HTTPServer(ADDR)
    httpd.setApp(application)
    print("Serving HTTP on port 8000")
    httpd.serveForever()

if __name__=="__main__":
    main()
