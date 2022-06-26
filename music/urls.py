# -*- codeing = utf -*-
# @Time : 2022/6/26 20:41
# @Author : 陈迪曙
# @File : urls.py
# @software : PyCharm
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.music_list, name='music_list'),
    path('list/<name>/', views.music, name='music_name')
]