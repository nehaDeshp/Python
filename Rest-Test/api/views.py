# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import TalkSerializer
from talkMethods.models import Talk
from rest_framework.response import Response

from django.shortcuts import render

# Create your views here.
@api_view(['GET','POST'])
def talk_list(request):

    if(request.method == 'GET'):
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks,many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = TalkSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetTalkWithID(request, id):
    if request.method == 'GET':
        queryset = Talk.objects.get(pk=id)
        serializer = TalkSerializer(queryset)
        return Response(serializer)

@api_view(['POST'])
def InsertTalk(request):
    if request.method == 'POST':
        serializer = TalkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def UpdateTalk(request, id):
    if request.method == 'PUT':
        talks = Talk.objects.get(pk=id)
        serializer = TalkSerializer(talks)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteTalk(request, id):
    if request.method == 'DELETE':
        queryset = Talk.objects.get(pk=id)
        serializer = TalkSerializer(queryset)
        if serializer.is_valid():
            serializer.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)