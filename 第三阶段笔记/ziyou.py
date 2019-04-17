from socket import *
import sys
import re
from threading import Thread
class HTTPServer(object):
    def __init__(self,app):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.app=app
    def bind(self,addr):
        self.sockfd.bind(addr)
    def start(self):
        self.sockfd.listen(10)
        while True:
            c,addr=self.sockfd.accept()
            print(addr,"用户连接")
            hanle_thread=Thread(target=self.handle_clent,argt=(c,))
            handle_thread.start()

    def hanle_client(self,c):
        request_data=c.recv(2048)
        request_liens=request_data.splitlies()
        request_line=request_lines[0].decode('utf-8')
        print(request_line)
        method=re.match(r'(\w+)\s+/\S*',request_line).group(1)
        filename=re.match(r'\w+\s+(/\S*)',request_line).group(1)
        env={'METHOD':method,'PATH_INFO':filename}
        response_body=self.app(env,self.set_headers)
        resonse=self.response_headers+'\r\n'+response_body
        c.send(response.encode())
        c.close()
    def set_hesders(self,status,headers):
        response_headers="HTTP/1.1"+status+"\r\n"
        for header in headers:
            response_hesders+="%s: %s\r\n"%header
        self.response_headers=reoponse_headers

def main():
    if len(sys.argv)<2:
        sys.exit('''run the server as :python3 httpserver framewormewordname:app''')

    module_name,app_name=sys.argv[1].split(":")
    sys.path.insert(1,".")
    m=__import__(module_name)
    app=getattr(m,app_name)
    htt_server=HTTPServer(app)
    http_server.bind(('0.0.0.0',8000))
    print("Listen on port 8000")
    http_server.start()
if __name__=="__main__":
    main()


