from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def homepage(request):
    customer = Post.objects.all()
    context = {'customer': customer}
    return render(request, 'microblog/home.html', context)


def blogpage(request):
    return render(request, 'microblog/blog.html')
