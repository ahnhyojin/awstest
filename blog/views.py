from django.shortcuts import render, redirect, get_object_or_404
from . models import Blog, Comment
from django.utils import timezone


# Create your views here.
def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs': blogs})

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['fulltext']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))

def detail(request, post_pk):
    post = get_object_or_404(Blog, pk=post_pk)
    return render(request, 'detail.html', {'posts' : post})

