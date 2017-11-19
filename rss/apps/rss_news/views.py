from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.


def index(request):

    number = random.randrange(0, 100)

    context = {
        'value': 'Hello Python!',
        'number': str(number)
    }

    return render(request, "index.html", context)