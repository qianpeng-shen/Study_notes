from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class Show(RequestHandler):
    def get(self, *args, **kwargs):
        html=('<form method=post action=/login enctype=multipart/form-data>'
                   '用户名：<input type=text name=uname><br>'
                   '密&nbsp;码: <input type=password name=uwd><br>'
                    '<input type=file name=avatar><br>'
                    '<input type=file name=avatar><br>'
                   '<input type=submit value=提交>&nbsp;&nbsp;&nbsp;&nbsp;'
                   '<input type=reset value=重置>'
                   '</form>')
        fahtml=('<form method=post action=/login>'
                   '用户名：<input type=text name=uname><br>'
                   '密&nbsp;码: <input type=password name=uwd><br>'
                    '<span style="color:red;">用户名或密码错误</span><br>'
                   '<input type=submit value=提交>&nbsp;&nbsp;&nbsp;&nbsp;'
                   '<input type=reset value=重置>'
                   '</form>')
        msg=self.get_query_argument('msg',None)
        if msg:
            self.write(fahtml)
        else:
            self.write(html)

    def post(self, *args, **kwargs):
        pass



define('kou',type=int,default=8888)
parse_config_file('../config/config')


class Login(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        a=self.get_body_argument('uname',None)
        b=self.get_body_argument('uwd',None)
        if a=="abc" and b=='123':
            self.redirect('/blog?uname='+a)
            #如果用户上传了文件
            #把文件保存到服务器上
            #self.request是RequestHandler
            #的一个属性，引用HttpServerRequst对象
            #该对象中封装了与请求相关的所有内容
            print(self.request)
            #HttpServerRequest对象的files属性
            #引用这用户表达上传的文件
            #如果用户没有上传文件，files属性是空字典
            #如果上传了文件
            #{'avatar':"[{'content_type':image/jpeg,
            # 'body':二进制格式表示的图像的内容,
            # 'filename':上传者本地图像名称},
            # {},
            # {}]}
            print(self.request.files)
            if self.request.files:
                avs=self.request.files['avatar']
                for a in avs:
                    body = a['body']
                    #上传的这一个文件内容保存在服务器的硬盘上
                    writer=open('upload/%s'%a['filename'],'wb')
                    writer.write(body)
                    writer.close()
        else:
            self.redirect('/?msg=fail')


class Bolg(RequestHandler):
    def get(self, *args, **kwargs):
        uname=self.get_query_argument('uname',None)
        if uname:
            self.write('欢迎'+uname+'使用')
        else:
            self.write('欢迎使用')
    def post(self, *args, **kwargs):
        pass


app=Application(handlers=[("/",Show),
                          ('/login',Login),
                          ('/blog',Bolg)])
server=HTTPServer(app)
server.listen(options.kou)
IOLoop.current().start()
