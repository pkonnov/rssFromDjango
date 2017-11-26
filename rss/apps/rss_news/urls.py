from django.conf.urls import url, include
from django.contrib import admin
from rss.apps.rss_news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/(?P<index>[0-9]+)/$', views.post, name='post_more'),
]
