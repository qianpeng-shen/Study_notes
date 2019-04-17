from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.write('<a href=/java>Try try Java</a>')
        self.write('<br>')
        self.write('<a href=/python>Try try Python</a>')
    def post(self,*args,**kwargs):
        pass

define('duankou',type=int,default=8888)
parse_config_file('../config/config')


class JavaHandler(RequestHandler):
    def get(self, p1=None, p2=None,*args, **kwargs):
        self.write('hello Java<br>')
        if p1:
            self.write('今天是：'+p1+'<br>')
        if p2:
            self.write('课程：'+p2)
    def post(self, *args, **kwargs):
        pass


class PythonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello pyhton')
        #获取参数
        d=self.get_query_argument('day',None)
        s=self.get_query_argument('subject',None)
        ds=self.get_query_arguments('day')
        ss = self.get_query_arguments('subject')
        print(d,s)
        print(ds,ss)
    def post(self, *args, **kwargs):
        self.write('hello python POST')
        d=self.get_body_argument('day',None)
        s=self.get_body_argument('subject',None)
        print(d,s)
        ds=self.get_body_arguments('day')
        ss=self.get_body_arguments('subject')
        print(ds,ss)
        #self.get_argument(s)=get_auery_argument+det_body_arguemnts
        arg_d=self.get_arguments('sub',None)
        arg_ds=self.get_arguments('subject')
        print(arg_d,arg_ds)



app=Application(handlers=[("/",IndexHandler),
                          ('/java',JavaHandler),
                          ('/java/(day[0-9]+)',JavaHandler),
                          ('/java/(day[0-9]+)/([a-z0-9]+)',JavaHandler),
                          ('/python',PythonHandler)])


server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()


