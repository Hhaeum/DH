from django.shortcuts import render, redirect
from .models import Dongne1
from .models import Dongne2
from django.core.paginator import Paginator

def index(request):

    return render(request,'index.html')

def daegu(request):
    return render(request,'daegu.html')

def gyeongsan(request):
    return render(request,'gyeongsan.html')

def create(request): 
    if request.method == "GET":
        lat = request.GET['lat']
        lng = request.GET['lng']
        context={
            "lat":lat,
            "lng":lng,
        }
        return render(request,'create.html',context)

    elif request.method == "POST":
        post = Dongne1()
        post.user = request.user
        post.title = request.POST['title']
        post.content = request.POST['content'] 
        post.pic = request.FILES.get('pic','default')
        post.lng = request.POST['lng'] 
        post.lat = request.POST['lat'] 
        post.save()
        return redirect('index')

def read(request,post_id): 
    post = Dongne1.objects.get(id = post_id)
    context={
        "post":post
    }
    return render(request,'read.html',context)

def CService(request): 
    post = Dongne2.objects.all()
    paginator = Paginator(post,5) 
    now_page = request.GET.get('page')
    post = paginator.get_page(now_page)
    context={ 
        "post":post,  
        }
    return render(request,"CService.html",context)

def CScreate(request):
    if request.method == "GET":
        return render(request,'CScreate.html')

    elif request.method == "POST":
        post = Dongne2()
        post.user=request.user
        post.title2 = request.POST['title']
        post.content2 = request.POST['content']
        anonymous = request.POST.get('anonymous',False)  
        if anonymous == "y":
            post.anonymous2 = True
        try:
            post.pic2=request.FILES['pic']
        except:
            pass
        post.category2=request.POST['category']
        post.save()

        return render(request,'index.html')

def CSread(request,post_id): 
    post = Dongne2.objects.get(id = post_id)
    context={
        "post":post
    }
    return render(request,'CSread.html',context)

def CSupdate(request,post_id):  
    if request.method == "GET":
        post = Dongne2.objects.get(id = post_id)
        context = {
            "post":post,
        }
        return render(request,'CSupdate.html',context)

    elif request.method == "POST":
        post = Dongne2.objects.get(id = post_id)
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category=request.POST['category']
        post.save()

        return redirect(index)

def CSdelete(request,post_id):
    post = Dongne2.objects.get(id=post_id)
    post.delete()
    return redirect(index)
# Create your views here.