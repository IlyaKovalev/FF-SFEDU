from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('program',views.program,name='program'),
    path('single',views.single,name='single'),
    path('All_lecturers',views.All_lecturers,name='All_lecturers'),
    path('lecturers/<int:lecturer_id>/',views.lecturers,name='Lecturer'),
    path('department/<int:department_id>/',views.department,name='department'),
]
