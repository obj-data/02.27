import re

from django.shortcuts import render

# Create your views here.
from .serializers import UserCreateSerializer
from rest_framework import response, decorators, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response

# from rest_framework_simplejwt.tokens import RefreshToken

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def registered(request):
    username = request.data['username']
    if len(username) > 18 or len(username) < 2:
        return Response('用户名不能小于2或大于18', status=status.HTTP_400_BAD_REQUEST)
    authUser = User.objects.filter(username=username)
    authEmail = User.objects.filter(email=request.data['email'])
    if authUser:
        return response.Response('用户名已存在', status=status.HTTP_400_BAD_REQUEST)
    elif authEmail:
        return response.Response('邮箱已存在', status=status.HTTP_400_BAD_REQUEST)
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        if re.findall(".*string='(.*?)'", str(serializer.errors))[0] == 'Enter a valid email address.':
            return response.Response('请输入正确的邮箱!', status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return response.Response(True, status=status.HTTP_201_CREATED)
