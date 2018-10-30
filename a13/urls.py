from django.conf.urls import url,include
from django.urls import path,re_path
from . import views
from .views import *
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home),
    #url(r'^',views.data),
    #url(r'^detail',views.home),
    re_path('home/index2/(?P<token_id>[\w\.-@+]+)/',views.data),
    path('login1',login1,name="login1"),
    path('index1',index1,name="index1"),
    path('home',home,name="home"),
    path('a',a,name="a"),
    url(r'^login1',views.login1),
    url(r'^login2',views.login2),
    url(r'^home',views.home),
    url(r'^logins',views.logins),
    url(r'^Events',views.Events),
    url(r'^TimetableG',views.TimetableG),
    url(r'^TA_a',views.TA_a),
    url(r'^Viewfm',views.Viewfm),
    url(r'^RescheduleC',views.RescheduleC),
    url(r'^index',views.index),
    #url(r'^index1',views.index1),
    #url(r'^index2',views.index2),
    url(r'^posts',views.posts),
    url(r'^profile',views.profile),
    url(r'^settings',views.settings),
    url(r'^users',views.users),
    url(r'^scheduleE',views.scheduleE),
    url(r'^schedulefm',views.schedulefm),
    url(r'^secheduled',views.secheduled),
]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


