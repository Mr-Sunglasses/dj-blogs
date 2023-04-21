from django.shortcuts import render
from django.http import HttpResponse
import datetime
from posts.models import Post

# Create your views here.

def welcome(request):
    context = {
        "current_time": datetime.datetime.now(),
        "posts": Post.objects.all(),
        "num_posts": Post.objects.count(),
    }
    return render(request, "blog/index.html", context=context)
