from django.shortcuts import render

# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost



def archive(request):
    posts = BlogPost.objects.all()

    return render(request,"archive.html",{'posts': posts})    #通过ORM获取数据库内容，并渲染之，作为应答报文返回







