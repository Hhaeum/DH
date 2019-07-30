from django.shortcuts import render, redirect
from .models import Blog
from django.core.paginator import Paginator

def index(request):

    return render(request,'index.html')

def daegu(request):
    return render(request,'daegu.html')

def gyeongsan(request):
    return render(request,'gyeongsan.html')

def create(request): 
    if request.method == "GET":
        return render(request,'create.html')

    elif request.method == "POST":
        post = Blog()
        post.title = request.POST['title']
        post.content = request.POST['content'] 
        post.save()
        return redirect(index)

def read(request,post_id): 
    post = Blog.objects.get(id = post_id)
    context={
        "post":post
    }
    return render(request,'read.html',context)

def CService(request): 
    posts = Blog.objects.all()
    paginator = Paginator(posts,1) 
    now_page = request.GET.get('page')
    posts = paginator.get_page(now_page)
    context={ 
        "posts":posts,  
        }
    return render(request,"CService.html",context)

def CScreate(request):
    if request.method == "GET":
        return render(request,'CScreate.html')

    elif request.method == "POST":
        post = Blog()
        post.user=request.user
        post.title = request.POST['title']
        post.content = request.POST['content']
        try:
            post.pic=request.FILES['pic']
        except:
            pass
        post.category=request.POST['category']
        post.save()

        return render(request,'CService.html')

def CSread(request,post_id): 
    post = Blog.objects.get(id = post_id)
    context={
        "post":post
    }
    return render(request,'CSread.html',context)
# Create your views here.
