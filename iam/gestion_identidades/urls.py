
from django.contrib import admin
from django.urls import path, include
#from .views import home
from . import views
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework import routers

urlpatterns = [
   
    #path('base', views.base, name='base'),
    path('', views.home, name='casita'),
    path('login', views.home, name='inicio'),
    path('registro', views.registro_usuario, name='registro'),
    #path('login', views.logout, name='logout'),
   
  
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)