from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *


# Create your views here.
def a_views(request):
    form=LoginForm()
    return render(request,'01_var.html',locals())

def login_views(request):
    form=LoginForm()
    if request.method=="GET":
    #判断cookies中是否有id和uphone
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            return HttpResponse('欢迎'+request.COOKIES['uphone']+'回来')
        else:
            return render(request,'01_var.html',locals())
    else:
        uphone=request.POST['uphone']
        upwd=request.POST['upwd']
        users=User.objects.filter(uphone=uphone,upwd=upwd)
        if users:
            resp=HttpResponse('登录成功')
            if 'isSaved' in request.POST:
                MAX_AGE=60*60*24*366
                resp.set_cookie('id',users[0].id,MAX_AGE)
                resp.set_cookie('uphone',uphone,MAX_AGE)
            return resp
        else:
            return render(request,'01_var.hmtl',locals())

def register_views(request):
    if request.method =="GET":

        return render(request,'02_var.html')
    else:
        #接受用户手机号，判断号码是否存在
        uphone=request.POST['uphone']
        users=User.objects.filter(uphone=uphone)
        if users:
            #手机号已经注册过，给出提示，回到注册界面
            errMsg='手机号码已经注册'
            return render(request,'02_var.html',locals())
        else:
            upwd=request.POST['upwd']
            uname=request.POST['uname']
            uemail=request.POST['uemail']
            User.objects.create(uphone=uphone,upwd=upwd,uname=uname,uemail=uemail)
            return HttpResponse('注册成功')



