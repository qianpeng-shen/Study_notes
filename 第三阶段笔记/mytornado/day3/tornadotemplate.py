import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule


class Show(RequestHandler):
    def get(self, *args, **kwargs):

        # r=''
        # msg=self.get_query_argument('msg',None)
        # if msg:
        #     r='用户名或密码错误'
        self.render('login.html')




    def post(self, *args, **kwargs):
        pass



define('shen',type=int,default=8888)
parse_config_file('../config/config')


class Login(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        a=self.get_body_argument('uname',None)
        b=self.get_body_argument('uwd',None)
        if a=="abc" and b=='123':
            self.redirect('/blog?uname='+a)

        else:
            self.redirect('/?msg=fail')


class Bolg(RequestHandler):

    def get(self, *args, **kwargs):

        self.render('blog.html',)



    def post(self, *args, **kwargs):
        pass


class LoginModule(UIModule):
    def render(self, *args, **kwargs):
        print(self.request)
        print(self.request.uri)#uri=路径+参数
        print(self.request.path)#uri中的路径
        print(self.request.query)#uri中的参数
        r=''
        if self.request.query:
            r='用户名或密码错误'
        return self.render_string('mymodule/login_module.html',result=r)


class BolModule(UIModule):
    def render(self, *args, **kwargs):
        a = [{'author': '大旭旭',
                  'avatar': 'a.jpg',
                  'title': '办证',
                  'content': '联系电话13843819438',
                  'tags': 'IT教育',
                  'count': 8},
                 {
                     'author': '小康',
                     'avatar': 'a.jpg',
                     'title': '帅',
                     'content': '要想瘦，找小康，小康竭诚为您服务',
                     'tags': '健身',
                     'count': 0
                 },
                 {
                     'author': '小云',
                     'avatar': 'c.jpg',
                     'title': '可爱',
                     'content': '曾经的过眼纷纭，始终是记忆，余生要把握在自己的手中',
                     'tags': '瑜伽',
                     'count': 100
                 },
                 {
                     'author': '小胖',
                     'avatar': None,
                     'title': '胖的不要不要的',
                     'content': '胃是自己的，不要亏待自己',
                     'tags': '吃货',
                     'count': 50
                 }]
        return self.render_string('mymodule/bolgmoudule.html',blogs=a)


class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        pass


app=Application(handlers=[("/",Show),
                          ('/login',Login),
                          ('/blog',Bolg),
                          ('/regist',RegistHandler)],
                template_path='mytemplates',
                static_path='mystatics',
                ui_modules={'loginmodule':LoginModule,
                            'bolgmoudule': BolModule}
                )
server=HTTPServer(app)
server.listen(options.shen)
IOLoop.current().start()
