# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from web.views import *
from web.models import *
def hello(request):
    return render(request,'index.html')
def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',locals())
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def single(request):
    return render(request,'single.html')
