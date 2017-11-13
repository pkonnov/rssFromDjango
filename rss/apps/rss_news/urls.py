from django.conf.urls import url
from django.contrib import admin
from rss.apps.rss_news import views

urlpatterns = [
    url(r'^index$', views.index)
]
