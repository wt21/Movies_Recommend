# -*- coding: utf-8 -*-
# @Time : 2020/1/3 16:30 
# @Author :
from django.urls import path

from two import views

urlpatterns = [
    path('hi/',views.hi,name = 'hi'),
]