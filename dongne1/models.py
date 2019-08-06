from django.db import models
from django.contrib.auth.models import User

class dongne1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now = True)
    category = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to="image/",null=True)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=50,blank=True)

class Comment(models.Model):
    dongne1=models.ForeignKey(dongne1,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

