from django.shortcuts import render, redirect
from .models import Dongne1
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
        post = Dongne1()
        post.user = request.user
        post.title = request.POST['title']
        post.content = request.POST['content'] 
        try:
            post.pic = request.FILES['pic']
        except:
            pass
        post.save()
        return redirect('index')

def read(request,post_id): 
    post = Dongne1.objects.get(id = post_id)
    context={
        "post":post
    }
    return render(request,'read.html',context)

def CService(request): 
    posts1 = Dongne1.objects.all()
    paginator = Paginator(posts1,30) 
    now_page = request.GET.get('page')
    posts1 = paginator.get_page(now_page)
    context={ 
        "posts1":posts1,  
        }
    return render(request,"CService.html",context)

def CScreate(request):
    if request.method == "GET":
        return render(request,'CScreate.html')

    elif request.method == "POST":
        post1 = Dongne1()
        post1.user=request.user
        post1.title = request.POST['title']
        post1.content = request.POST['content']
        try:
            post1.pic=request.FILES['pic']
        except:
            pass
        post1.category=request.POST['category']
        post1.save()

        return render(request,'CService.html')

def CSread(request,post_id): 
    post = Dongne1.objects.get(id = post_id)
    context={
        "post":post
    }
    return render(request,'CSread.html',context)
# Create your views here.
