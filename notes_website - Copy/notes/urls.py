from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/',views.create,name='create'),
    path('mynotes/',views.mynotes,name='mynotes'),
]