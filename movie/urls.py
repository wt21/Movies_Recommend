# -*- coding: utf-8 -*-
# @Time : 2020/1/7 12:53 
# @Author :
from django.urls import path, re_path

from movie import views

urlpatterns = [
    path('hi/',views.hi)


]