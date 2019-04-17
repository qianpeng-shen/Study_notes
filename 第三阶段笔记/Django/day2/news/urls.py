from django.conf.urls import url
from .views import *

#当访问路径是http:localhost:8000/news/***
#则交给当前的urls.py去处理
urlpatterns=[
   #匹配访问路径是index的话，则交给index_views去处理
   #http://localhost:8000/news/index 
   # url(r'^index/$',index_views),
   #http://localhost:8000/news/
   url(r'^$',index_views),
   #http://localhost:8000/news/01_template/
   url(r'^01_template/$',template_views),
   #http://localhost:8000/news/02_render/
   url(r'^02_render/$',render_views),
   #http://localhost:8000/news/03_variable/
   url(r'^03_variable/$',var1_views),
   #http://localhost:8000/news/04_variable/
   url(r'^04_variable/$',var2_views),
   url(r'^05_variable/$',var3_views),
   url(r'06_tag/$',tag_views),
   url(r'07_static/$',static_views),
   url(r'08_parent',parent_views),
   #当前url的别名为child
   url(r'09_child',child_views,name="child"),
   url(r'10_name/$',name_views ),
   #http://localhost:8000/news/11_arg/四位数字/两位数字
   url(r'11_arg/(\d{4})/(\d{2})$',arg_views,name="arg"),

]