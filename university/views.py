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

def contact(request):
    context={}
    return render(request, 'university/contact.html', context)

def program(request):
    context={}
    return render(request, 'university/program.html', context)

def single(request):
    context={}
    return render(request, 'university/single.html', context)    
