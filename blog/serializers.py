# -*- codeing = utf -*-
# @Time : 2022/2/27 15:06
# @Author : 陈迪曙
# @File : serializers.py
# @software : PyCharm
from rest_framework import serializers
from .models import Blog


# 创建blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('username', 'title', 'body', 'date', 'owner')


# 查看blog
class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('username', 'title', 'body', 'date')
