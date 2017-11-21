from django.http import HttpResponse
from django.shortcuts import render
from rss.apps.rss_news.models import Post

# Create your views here.


def index(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, "index.html", context)