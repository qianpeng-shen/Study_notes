#多进程tcp
from socketserver import *

class Server(ForkingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        #self.request 相当于 accpet创建的新的套接字
        addr=self.request.getpeername()
        print("Connect from ",addr)
        while True:
            data=self.request.recv(1024).decode()
            if not data:
                break
            self.request.send(b"receive your message")
server=Server(('127.0.0.1',9999),Handler)
server.serve_forever()