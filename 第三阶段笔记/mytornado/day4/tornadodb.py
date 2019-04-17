import json
import pymysql
import time

from os import remove
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule

from day4.util.myutil import mymd


class Show(RequestHandler):
    def get(self, *args, **kwargs):

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
        #1通过mysql建立于数据库的链接
        settins={'host':'127.0.0.1',
                 'port':3306,
                 'user':'root',
                 'password':'123456',
                 'database':'blog_db',
                 'charset':'utf8'}
        connection=pymysql.connect(**settins)

        #2通过连接获取游标
        cursor=connection.cursor()
        #3利用游标发送语句
        #这么写sql,可能会被注入攻击
        # sql='select count(*) from tb_user where user_name="%s" and user_password="%s"'%(a,b)
        sql='select count(*) from tb_user ' \
            'where user_name=%s and ' \
            'user_password=%s'
        pwd = mymd(b)
        params=(a,pwd)
        cursor.execute(sql,params)
        #4返回值
        # result=cursor.fetchall()
        result=cursor.fetchone()
        # print('result----->',result)
        if result[0]:
            self.redirect('/blog?uname'+a)
        else:
            self.redirect('/?msg=fail')



class Bolg(RequestHandler):

    def get(self, *args, **kwargs):

        self.render('blog.html')



    def post(self, *args, **kwargs):
        pass


class LoginModule(UIModule):
    def render(self, *args, **kwargs):

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
        username = self.get_body_argument('uname',None)
        password = self.get_body_argument('uwd',None)
        city = self.get_body_argument('city',None)

        if username and password and city:
            print(username,password,city)
            avatar = None
            if self.request.files:
                #{'avatar':[{'body','filename','content-type'},{}]}
                f = self.request.files['avater'][0]
                body = f['body']
                fname = str(time.time()) + f['filename']
                writer = open('mystatics/images/%s'%fname,'wb')
                writer.write(body)
                writer.close()
                avatar = fname

            settings={'host':'127.0.0.1',
                      'port':3306,
                      'user':'root',
                      'password':'123456',
                      'database':'blog_db',
                      'charset':'utf8'}
            connection = pymysql.connect(**settings)
            cursor = connection.cursor()
            sql='insert into tb_user(' \
                'user_name, ' \
                'user_password, ' \
                'user_avatar, ' \
                'user_city) ' \
                'values(%s,%s,%s,%s)'
            #将原始的password利用摘要算法(md)进行格式的转化
            # md=hashlib.md5()
            # md.update(password.encode('utf8'))
            # pwd=md.hexdigest()
            pwd=mymd(password)
            params = (username,pwd,avatar,city)
            try:
                cursor.execute(sql,params)
                #提交！！！
                cursor.connection.commit()
            except Exception as e:
                if avatar:
                    remove('mystatics/images/%s'%avatar)
                err = str(e)
                #(1062, "Duplicate entry 'abc' for key 'user_name'")
                code = err.split(',')[0].split('(')[1]
                r=''
                if code == '1062':
                    r = 'duplicate'
                else:
                    r = 'dberror'

                self.redirect('/regist?msg='+r)
            else:
                self.redirect('/')

        else:
            self.redirect('/regist?msg=empty')


class RegistModle(UIModule):
    def render(self, *args, **kwargs):
        r = ''
        if self.request.query:

            err=self.request.query.split('=')[1]
            if err=='empty':
                r='请输入完整'
            if err=='duplicate':
                r='用户名重复'
            if err=='dberror':
                r='数据库错误'

        return self.render_string('mymodule/regist_module.html',result=r)



app=Application(handlers=[("/",Show),
                          ('/login',Login),
                          ('/blog',Bolg),
                          ('/regist',RegistHandler)],
                template_path='mytemplates',
                static_path='mystatics',
                ui_modules={'loginmodule':LoginModule,
                            'bolgmoudule': BolModule,
                            'registmodule':RegistModle}
                )
server=HTTPServer(app)
server.listen(options.shen)
IOLoop.current().start()
