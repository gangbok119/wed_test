

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from .forms import PostForm
from .models import Post


def post_list(request):
    posts=Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request,'post/post_list.html',context)

def post_detail(request,pk):
    post=Post.objects.get(pk=pk)
    context={
        'post':post
    }
    return render(request,'post/post_detail.html',context)

def post_create(request):
    if request.method=='POST':
        title =request.POST['title']
        text = request.POST['text']
        user = User.objects.first()
        Post.objects.create(title=title,text=text,author=user)
        return redirect('post_list')
    else:
        return render(request,'post/post_create.html',)

def post_delete(request,pk):
    if request.method =="POST":
        post=Post.objects.get(pk=pk)
        post.delete()
        return redirect('post_list')
    else:
        return render(request,'post/post_list.html')