from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('index.html',views.index,name='index'),
    path('about.html',views.about,name='about'),
    path('gallery.html',views.gallery,name='gallery'),
    path('blog.html',views.blog,name='blog'),
]
