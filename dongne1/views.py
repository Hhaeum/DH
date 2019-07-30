from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator

def index(request):

    return render(request,'index.html')

def daegu(request):
    return render(request,'daegu.html')

def CService(request): 
    posts = Blog.objects.all()
    paginator = Paginator(posts,1) 
    now_page = request.GET.get('page')
    posts = paginator.get_page(now_page)
    context={ 
        "posts":posts,  
        }
    return render(request,"CService.html",context)
# Create your views here.
