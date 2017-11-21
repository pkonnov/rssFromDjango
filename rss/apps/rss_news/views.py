from django.http import HttpResponse
from django.shortcuts import render
from rss.apps.rss_news.models import Post

# Create your views here.


def index(request):

    posts = reversed(Post.objects.all())

    context = {
        'posts': posts
    }

    return render(request, "index.html", context)



def post(request, index):
	try:
		post = Post.objects.get(id=index)
		result = post.text
	except Post.DoesNotExist:
		result = "Does not exist"
	return HttpResponse(result)