from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import UserAccountSerializer
from .models import UserAccount


class  UserAccountViewset(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class =  UserAccountSerializer
