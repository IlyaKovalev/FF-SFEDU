from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def index(request):
    context={}
    return render(request, 'university/index.html', context)

def about(request):
    context={}
    return render(request, 'university/about.html', context)

def gallery(request):
    context={}
    return render(request, 'university/gallery.html', context)

def blog(request):
    context={}
    return render(request, 'university/blog.html', context)    
