# -*- coding: utf-8 -*-
# @Time : 2020/1/3 16:08 
# @Author :
from django.urls import path, re_path

from APP import views

urlpatterns = [
    path('login/',views.login,name = 'login'),
    path('logout',views.logout,name = "logout"),
    path('register/',views.register,name = 'register'),
    path('checkUser/',views.check_user,name = 'check_user'),
    path('show_index/',views.show_index,name = 'show_index'),
    path('index/',views.index,name = 'index'),
    path('search/',views.search,name = 'search'),
    path('test/',views.test,name = 'test'),
    path('show_movie/<movie_num>/',views.show_movie,name = 'show_movie'),
    path('show_recommend/',views.show_recommend,name = 'show_recommend'),
    path('tt/',views.tt),
    path('score/',views.score,name = 'score'),
    path('your_score/',views.your_score,name = 'your_score'),
    path("test/",views.test,name = "test"),
    path('del_score',views.del_score,name = 'del_score'),
]