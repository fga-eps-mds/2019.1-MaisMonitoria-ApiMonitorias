from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import UserAccount
from .serializers import UserAccountSerializer
from .models import InterestArea
from .serializers import InterestAreaSerializer

class  UserAccountViewset(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class =  UserAccountSerializer

class  InterestAreaViewset(ModelViewSet):
    queryset = InterestArea.objects.all()
    serializer_class =  InterestAreaSerializer