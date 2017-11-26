from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
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
		previous_id = post.id - 1
		next_id = post.id + 1
		context = {
			'post': post,
			'previous_id': previous_id,
			'next_id': next_id,
			'max_id': len(Post.objects.all())
		}
		return render(request, "post_more.html", context)
	except Post.DoesNotExist:
		result = "Does not exist"
		return HttpResponse(result)

def login(request):
	return render(request, "login.html")


def register(request):
	return render(request, "registration.html")


def register_user(request):
	if request.POST:
		user_name = request.POST["user_name"]
		email = request.POST["email"]
		password = request.POST["password"]
		repeat_password = request.POST["repeat_password"]
		return HttpResponseRedirect("/")
	else:
		return HttpResponse(result)


def check_user_name(request):
	if request.GET:
		user_name = request.GET["user_name"]

		names = set(["Odmin", "Eblo", "Petuh", "Vanychka"]) # (), {}
		if user_name in names:
			return HttpResponse("no", content_type='text/html')
		else:
			return HttpResponse("ok", content_type='text/html')

	else:
		return HttpResponse("no", content_type='text/html')