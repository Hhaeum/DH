from django.shortcuts import render, redirect
from .models import Blog
from django.core.paginator import Paginator

def index(request):

    return render(request,'index.html')

def daegu(request):
    return render(request,'daegu.html')

def gyeongsan(request):
    return render(request,'gyeongsan.html')

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
# Create your views here.
