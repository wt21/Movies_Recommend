# -*- coding: utf-8 -*-
# @Time : 2020/1/3 16:08 
# @Author :
from django.urls import path, re_path

from APP import views

urlpatterns = [
    path('hello/',views.hello,name = 'hello'),
    path('login/',views.login,name = 'login'),
    path('logout',views.logout,name = "logout"),
    path('register/',views.register,name = 'register'),
    path('checkUser/',views.check_user,name = 'check_user'),
    path('show_index/',views.show_index,name = 'show_index'),
    path('index/',views.index,name = 'index'),
]