from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request, "blog/home.html",{'posts':posts})
def about(request):
    return render(request, "blog/about.html")