from django.contrib import admin
from django.urls import path, include
from . import  views
urlpatterns = [
    path('', views.index),
    path('select_moive/', views.select_moive,name="select_moive"),
    path('select_page/', views.select_page,name="select_page"),
    path('select_contain/', views.select_contain,name="select_contain"),

]
