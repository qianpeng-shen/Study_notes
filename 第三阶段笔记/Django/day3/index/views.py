from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.db.models import F,Q

# Create your views here.
def add_views(request):
    Author.objects.create(name='laoshe',age=65,email='laoshe@163.com')
    obj=Author(name='zhuziqing',age=62,email='zhuziqing@163.com')
    obj.save()
    dic={
        'name':'luxun',
        'age':60,
        'email':'luxun@163.com'
    }
    obj=Author(**dic)
    obj.save()
    return HttpResponse("OK")
    #Publisher.objects.create(name='luoguanzhong',address='bejingdaxuechubanshe',city='beijing',country="zhongguo",website="")
def query_views(request):
    #auList=Book.objects.all()
    #print(auList
    #for au in auList:
    #    print(au.title,",",au.publicate_date)
    # auto=Book.objects.values('title','publicate_date')
    # print(auto)
    # for au in auto:
    #     print(au['title'],au['publicate_date'])
    # aulist=Book.objects.values_list('title','publicate_date')
    # print(aulist)
    # aulist=Book.objects.all().values('title')
    # for i in aulist:
    #     print(i)

    #查询排序：order_by()
    # aulist=Book.objects.all().order_by('-publicate_date')
    # # print(aulist)
    # for au in aulist:
    #     print(au.id,",",au.title,",",au.publicate_date)

    #对条件取反：exclude(条件)
    # aulist=Book.objects.exclude(id=1,title="xiyouji")
    # for ar in aulist:
    #     print(ar.id,",",ar.title,",",ar.publicate_date)

    #查询title包含an的记录
    # aulist=Book.objects.filter(title__contains='an')
    # for i in aulist:
    #     print(i.id,",",i.title,",",i.publicate_date)

    # au=Author.objects.get(id=1)
    # au.name="pingxin"
    # au.age=100
    # au.email="pingxin@163.com"
    # au.save()
    Author.objects.all().update(age=75)
    return HttpResponse("Query Ok")





def aulist_views(request):
    auList=Author.objects.filter(isActive=True)
    return render(request,'01_aulist.html',locals())
def delete_views(request,id):
    # Author.objects.get(id=id).delete()
    # return HttpResponse('删除成功')
    au=Author.objects.get(id=id)
    au.isActive=False
    au.save()
    #转发
    # return aulist_views(request)
    #重定向
    return HttpResponseRedirect('/03_aulist/')




def upshow_views(request,id):
    au=Author.objects.get(id=id)
    return render(request,'02_update.html',locals())








def upage_views(request):
    #修改所有人的年龄加十岁
    Author.objects.all().update(age=F('age')+10)
    return HttpResponseRedirect('/03_aulist/')
def doQ_views(request):
    auList=Author.objects.filter(Q(id=6)|Q(age__gte=70),isActive=True)
    return render(request,"01_aulist.html",locals())
def raw_views(request):
    sql='select * from index_author where id>=8;'
    auList=Author.objects.raw(sql)
    # print(auList)
    for au in auList:
        print(au.name,",",au.age)
    return HttpResponse("Execute raw success!")
def oto_views(request):
    #获取id为1的 wife的信息
    wife=Wife.objects.get(id=1)
    #在获取wife对应的Author
    author=wife.author

    #反向查询
    author=Author.objects.gt(id=14)
    wife=author.wife

    return recder(request,'03_oto.html',locals())
def otm_views(request):
    #查询id为1的书籍的信息
    # book=Book.objects.get(id=1)
    #查询该图书关联的出版社
    # publisher=book.publisher

    #查询id为1的Publisher的信息
    publisher=Publisher.objects.get(id=1)
    #查询该出版社所关联的所有的图书
    books=publisher.book_set.all()

    return render(request,'04_otm.html',locals())
def mtm_views(request):
    #通过 author 查询所有的book
    author=Author.objects.get(id=10)
    books=author.book.all()

    book=Book.objects.get(id=1)
    authors=book.author_set.all()

    return render(request,'05_mtm.html',locals())
def mta_views(request):
    author=Author.objects.get(name="韩寒")
    publishers=author.publisher.all()

    publisher=Publisher.objects.get(name="北京大学出版社")
    authors=publisher.author_set.all()
    return render(request,'06_mta.html',locals())
def obj_views(request):
    count=Author.objects.auCount()
    return HttpResponse(count)
def tit_views(request):
    filt=Author.objects.ltage(80)
    for i in filt:
        print(i.name)
    titl=Book.objects.titlecontains('西')
    for i in titl:
        print(i.title)
    return HttpResponse("ok")


def update_views(request):
    id=request.POST['id']
    names=request.POST['names']
    age=request.POST['age']
    email=request.POST['email']

    au=Author.objects.get(id=id)
    au.names=names
    au.age=age
    au.email=email
    au.save()
    return HttpResponseRedirect('/03_aulist/')