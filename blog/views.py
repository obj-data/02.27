from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from .serializers import BlogSerializer, BlogListSerializer
from .models import Blog
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse


# Create your views here.

def test_user(request):
    if request.user.get_username() == '':
        return Response('未登录用户不允许创建博客', status=status.HTTP_400_BAD_REQUEST)
    request.data['owner'] = User._get_pk_val(request.user)
    request.data['username'] = User.get_username(request.user)
    serializer = BlogSerializer(data=request.data)
    return serializer


class BlogUserList(generics.ListAPIView):
    '''
    get: 获取用户自己的所有博客

    post: 新建博客
    '''
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def post(self, request):
        serializer = test_user(request=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if request.user.get_username() == '':
            raise Http404()
        username = self.request.user.get_username()
        data = Blog.objects.filter(username=username).values('username', 'title', 'body', 'date')
        return Response(data)


class BlogList(generics.ListAPIView):

    '''
    get: 获取所有blog
    post: 废弃
    '''
    queryset = Blog.objects.values('username', 'title', 'body', 'date')
    serializer_class = BlogListSerializer

    def post(self):
        raise Http404


# 修改个人博客，覆盖式修改(未完成)
@api_view(['PUT', 'DELETE'])
def blog_detail(request, title):
    try:
        blog = Blog.objects.get(title=title)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = test_user(request=request)
        if serializer.is_valid():
            serializer.save()
            return Response('修改成功', status=status.HTTP_201_CREATED)
