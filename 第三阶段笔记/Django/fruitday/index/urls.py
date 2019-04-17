from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^login/$',login_views,name="login"),
    url(r'^$',a_views),
    url(r'^register/$',register_views,name="register"),
    # url(r'^regis/$',regis_veiws,name="regis"),
    
]