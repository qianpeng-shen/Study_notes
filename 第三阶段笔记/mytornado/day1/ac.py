from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class Login(RequestHandler):
    def get(self, *args, **kwargs):
        html=('<form action=/login method=post enctype=multipart/form-data>'
              '用户名:<input type=text name=uname><br>'
              '密码:<input type=password name=uwp><br>'
              '<input type=file name=avatar><br>'
              '<input type=file name=avatar><br>'
              '<input type=submit value=提交>'
              '<input type=reset value=重置>'
              '</form>')
        fahtml=('<form action=/login method=post>'
              '用户名:<input type=text name=uname><br>'
              '密码:<input type=password name=uwp><br>'
              '<span style="color:red;">用户名或密码错误</span><br>'
              '<input type=file name=avatar><br>'
              '<input type=file name=avatar><br>'
              '<input type=submit value=提交>'
              '<input type=reset value=重置>'
              '</form>')
        msg=self.get_query_argument('msg',None)
        if msg:
            self.write(fahtml)
        else:
            self.write(html)
    def post(self, *args, **kwargs):
        pass


class Show(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        a=self.get_body_argument('uname',None)
        b=self.get_body_argument('uwp',None)
        if a=='abc' and b=='123':
            self.redirect('/blog?uname='+a)
            print(self.request)
            print(self.request.files)
            if self.request.files:
                avs=self.request.files['avatar']
                for a in avs:
                    body = a['body']
                    #上传的这一个文件内容保存在服务器的硬盘上
                    writer=open('ab/%s'%a['filename'],'wb')
                    writer.write(body)
                    writer.close()
        else:
            self.redirect('/?msg=fail')


class Bolog(RequestHandler):
    def get(self, *args, **kwargs):
        uname=self.get_query_argument('uname')
        if uname:
            self.write('欢迎'+uname+'使用')
        else:
            self.write('欢迎使用')
    def post(self, *args, **kwargs):
        pass


app=Application(handlers=[('/',Login),
                          ('/login',Show),
                          ('/blog',Bolog)])
server=HTTPServer(app)
server.listen(7485)
IOLoop.current().start()
