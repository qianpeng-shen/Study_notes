import time
HTML_ROOT_DIR="./static"
PYTHON_DIR="./wsgiPy"
class Application(object):
    def __init__(self,urls):
        self.urls=urls
    def __call__(self,env,set_headers):
        path=env.get('PARH_INFO','/')
        if path.startswith('static'):
            file_name=path[7:]
            try:
                fd=open(HTML_ROOT_DIR,'rb')
            except IOError:
                status='404 not fount'
                headers=[]
                set_headers(status,headers)
                return "<h1>===没找到===<h1>"
            else:
                file_data=fd.read()
                fd.close()
                status='200 OK'
                headers=[]
                set_headers(status,headers)
                return file_data.decode('utf-8')
        else:
            for url,handler in self.urls:
                if path==url:
                    return handler(env,set_headers)
            status="404 not found"
            headers=[]
            set_headers(status,headers)
            return "sorry url not found"
def show _time(env,set_headers):
    status="200 OK"
    headers=[]
    set_headers(status,headers)
    return time.ctime()
def show _time(env,set_headers):
    status="200 OK"
    headers=[]
    set_headers(status,headers)
    return time.ctime()
def show _time(env,set_headers):
    status="200 OK"
    headers=[]
    set_headers(status,headers)
    return time.ctime()
urls=[
    ('/time',show_time),
    ('/hello',say_hello),
    ('/bye',say_bye),
    ("/xiaoyang",yang)
]
app=Application(urls)
