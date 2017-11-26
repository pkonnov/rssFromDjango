from django.conf.urls import url, include
from django.contrib import admin
from rss.apps.rss_news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/(?P<index>[0-9]+)/$', views.post, name='post_more'),
    url(r'login/$', views.login, name='login'),
    url(r'registration/$', views.register, name='register'),
    url(r'registration_user/$', views.register_user, name='register_user'),
    url(r'check_user_name/$', views.check_user_name , name='check_user_name')
]
