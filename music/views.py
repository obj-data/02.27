from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from rest_framework.response import Response
# Create your views here.
import os
from rest_framework import status
from rest_framework.decorators import api_view
import base64

filePath = r"D:\musics"


@api_view(['GET'])
def music_list(request):
    names = []
    # 获取文件夹下的所有mp3文件名
    for i, j, k in os.walk(filePath):
        for name in k:
            names.append(name[2::]) if "mp3" in name else False
    body = {"names": names}
    return Response(body)


@api_view(['GET'])
def music(request, name):

    '''
    :param request:
    :param name: 歌曲名称
    :return: 歌曲字节
    '''
    print(name)
    music = open(filePath + "\\" + name, 'rb')
    response = FileResponse(music)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment;filename=music.mp3"
    return response
