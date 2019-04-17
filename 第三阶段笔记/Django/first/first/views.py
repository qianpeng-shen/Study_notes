from django.http import HttpResponse
#编写视图处理函数,一个函数相当于是一个视图
def run_views(request):
    #request主要封装的是请求信息
    return HttpResponse("<h1>你好,世界</h1>")
def run1_views(ruquest,num):
    return HttpResponse("传递的参数是:"+num)
def run2_views(ruquest,num1,num2):
    return HttpResponse("参数1:"+num1+",参数2:"+num2)
def show_views(request,name,age):
    return HttpResponse("参数1:"+name+",参数2:"+age)


