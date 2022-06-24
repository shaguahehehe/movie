from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('select_moive/', views.select_moive, name="select_moive"),
    path('select_page/', views.select_page, name="select_page"),
    path('select_contain/', views.select_contain, name="select_contain"),
    path('login/', views.login, name="login"),
    # 验证码
    re_path(r'yzm/[0-9]*', views.captcha, name='yzm'),
]
