# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import User_account
from .serializers import UserSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

users = {
    1: User_account(user_account_id='M', course='Engenharia de Software', description='des'),
}

class UserViewSets(viewsets.ViewSet):
    
    def list(self, request):
        serializer = UserSerializer(
            instance=User_account.objects.all(), many=True)
        return Response(serializer.data)

    def create(self ,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
