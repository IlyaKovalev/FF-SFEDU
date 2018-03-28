from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def index(request):
    lecturers = Lecturer.objects.all()
    lecturers = lecturers[0:2]
    departments = Department.objects.all()
    context={'lecturers':lecturers,'departments':departments}
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

def department(request,department_id):
    department = Department.objects.filter(id=department_id)[0]
    context={'department':department }
    return render(request, 'university/Department.html', context)
def All_lecturers(request):
    lecturers = Lecturer.objects.all()
    context={'lecturers':lecturers}
    return render(request, 'university/All_lecturers.html', context)
def lecturers(request,lecturer_id):
    lecturer= Lecturer.objects.filter(id=lecturer_id)
    lector=lecturer[0]
    context={'lector':lector, 'Name':lecturer[0].Name,'degree':lecturer[0].degree,
             'cathedra':lecturer[0].cathedra,'additional_info':lecturer[0].additional_info,
             'seniority':lecturer[0].seniority,'image':lecturer[0].image,
             'work':lecturer[0].work}
    return render(request,'university/wrapper/lecturers.html',context)
