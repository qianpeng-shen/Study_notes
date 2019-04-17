import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class Show(RequestHandler):
    def get(self, *args, **kwargs):

        r=''
        msg=self.get_query_argument('msg',None)
        if msg:
            r='用户名或密码错误'
        self.render('login.html',result=r)




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
    def set_default_headers(self):
        #让继承者自定义响应头中的内容
        print("set_default_headers方法被调用")
    def initialize(self):
        # 让继承者在执行get/post方法之前传入参数
        #或者执行一些初始化操作
        print("initialize方法被调用了")
    def on_finish(self):
        #执行get/post方法执行完毕后，释放资源
        print('on_finish方法被调用')

    def get(self, *args, **kwargs):
        print("get方法被调用")
        # uname=self.get_query_argument('uname',None)
        # if uname:
        #     self.write('欢迎'+uname+'使用<br>')
        #     self.write('今天星期一<br>')
        #     self.write('西班牙被淘汰了')
        # else:
        #     self.write('欢迎使用')

        #以JSON字符串作为响应内容
        #JSON格式：
        #必须用双引号 {"key":"value","key2":"value2"}
        # resp={'key1':'value1',
        #       'key2':'key2'}
        # self.write(resp)

        # Content - Type: application / json;
        # # charset = UTF - 8
        # self.set_header('Content-Type',
        #                  'application/json;charset=UTF-8')
        # json_str=json.dumps(resp)
        # self.write(json_str)




        self.render('blog.html',blogs=[{'author':'大旭旭',
                                        'avatar':'a.jpg',
                                        'title':'办证',
                                        'content':'联系电话13843819438',
                                        'tags':'IT教育',
                                        'count':8},
                                       {
                                        'author': '小康',
                                        'avatar': 'a.jpg',
                                        'title': '帅',
                                        'content': '要想瘦，找小康，小康竭诚为您服务',
                                        'tags': '健身',
                                        'count':0
                                       },
                                       {
                                           'author': '小云',
                                           'avatar': 'c.jpg',
                                           'title': '可爱',
                                           'content': '曾经的过眼纷纭，始终是记忆，余生要把握在自己的手中',
                                           'tags': '瑜伽',
                                           'count':100
                                       },
                                       {
                                           'author': '小胖',
                                           'avatar':None,
                                           'title': '胖的不要不要的',
                                           'content': '胃是自己的，不要亏待自己',
                                           'tags': '吃货',
                                           'count':50
                                       }])



    def post(self, *args, **kwargs):
        pass



app=Application(handlers=[("/",Show),
                          ('/login',Login),
                          ('/blog',Bolg)],
                template_path='mytemplates',
                static_path='mystatics')
server=HTTPServer(app)
server.listen(options.shen)
IOLoop.current().start()
