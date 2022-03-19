import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics, permissions
from .serializers import BlogSerializer, BlogListSerializer, BlogObjectSerializer
from .models import Blog
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from .authJWT import AuthToken
import json


# Create your views here.

def test_user(request):
    request.data['owner'] = User._get_pk_val(request.user)
    request.data['username'] = User.get_username(request.user)
    serializer = BlogSerializer(data=request.data)
    return serializer


class BlogUserList(generics.ListAPIView):
    authentication_classes = [AuthToken]
    '''
    get: 获取用户自己的所有博客(需登录)

    post: 新建博客(需登录)
    '''

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def post(self, request):
        print(request.user)
        serializer = None
        if test_user(request):
            serializer = test_user(request=request)
        else:
            return Response('只能修改自己创建的博客', status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(True, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        username = self.request.user.get_username()
        data = Blog.objects.filter(username=username).values('username', 'title', 'body', 'date')
        data = data.order_by('-date')
        blogs1 = []
        blogs1.extend(data)
        for i in range(len(blogs1)):
            if len(blogs1[i]['body']) > 100:
                blogs1[i]['body'] = blogs1[i]['body'].replace('\n', '')[0:99] + '......'
        return Response(blogs1)


class BlogList(generics.ListAPIView, ):
    '''
    (无需登录)
    get: 获取所有blog
    post: 废弃
    '''
    queryset = Blog.objects.values('username', 'title', 'body', 'date').order_by('-date')
    serializer_class = BlogListSerializer

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.values('username', 'title', 'body', 'date').order_by('-date')
        blogs1 = []
        blogs1.extend(blogs)
        for i in range(len(blogs1)):
            if len(blogs1[i]['body']) > 100:
                blogs1[i]['body'] = blogs1[i]['body'].replace('\n', '')[0:99] + '......'
        return Response(blogs1)

    def post(self, request):
        raise Http404


# 修改个人博客，覆盖式修改(未完成)
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, title):
    if request.method == 'GET':
        '''
        查看博客的详细内容
        :param request:
        :param title:
        :return:
        '''
        try:
            blog = Blog.objects.get(title=title)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = {'username': blog.username, 'title': blog.title, 'body': blog.body, 'date': blog.date}
        return Response(data)
    # if test_user(request):
    #     serializer = test_user(request=request)
    # else:
    #     return Response('请登录后再试', status=status.HTTP_400_BAD_REQUEST)
    request.user = AuthToken().authenticate(request)[0]
    '''
    修改或删除博客(需登录)
    '''
    try:
        blog = Blog.objects.get(title=title)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if str(request.user) != blog.username:
        return Response('你无权修改此博客', status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serializer = None
        if test_user(request):
            serializer = test_user(request=request)
        else:
            return Response('只能修改自己创建的博客', status=status.HTTP_400_BAD_REQUEST)
        blog.delete()
        if serializer.is_valid():
            blog.title = serializer.data['title']
            blog.body = serializer.data['body']
            blog.save()
            return Response('修改成功', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        blog.delete()
        return Response('删除博客成功!', status=status.HTTP_204_NO_CONTENT)
