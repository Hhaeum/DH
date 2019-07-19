from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def daegu(request):
    return render(request,'daegu.html')
# Create your views here.
