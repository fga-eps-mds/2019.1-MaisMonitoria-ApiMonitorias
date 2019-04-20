from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import UserAccount
from .serializers import UserAccountSerializer


class  UserAccountViewset(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class =  UserAccountSerializer