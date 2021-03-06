"""DH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import dongne1.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dongne1.views.index,name='index'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('daegu/',dongne1.views.daegu,name='daegu'),
    path('gyeongsan/',dongne1.views.gyeongsan,name='gyeongsan'),
    path('create/',dongne1.views.create,name='create'),
    path('CService/',dongne1.views.CService,name='CService'),
    path('CScreate/',dongne1.views.CScreate,name='CScreate'),
    path('CSread/<int:post_id>',dongne1.views.CSread,name='CSread'),
    path('read/<int:post_id>/',dongne1.views.read,name='read'),
    path('CSupdate/<int:post_id>',dongne1.views.CSupdate,name='CSupdate'),
    path('CSdelete/<int:post_id>',dongne1.views.CSdelete,name='CSdelete'),
    path('category2/',dongne1.views.category2,name='category2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
