# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models  import Blog,Author,Entry

# Create your views here.
import redis
def redis_home(request):

    obj= redis.StrictRedis(host='localhost',port=6379,db=0)
    r= Blog.objects.all(),Author.objects.all(),Entry.objects.all()
    obj.set("r",r)
    objset=obj.get("r")
    context ={
    "objset":objset
    }
    return render(request,"redis.html",context)
