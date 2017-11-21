from django.conf.urls import url
from django.contrib import admin
from rss.apps.rss_news import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'post/(?P<index>[0-9]+)/$', views.post)
]
