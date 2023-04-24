from django.contrib import admin
from django.urls import path,include
from .views import apiOverview, Post

urlpatterns = [
    path('',apiOverview,name='Api Overview'),
    path('post',Post,name='Post'),
]
