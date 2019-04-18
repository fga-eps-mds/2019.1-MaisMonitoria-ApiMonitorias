from rest_framework.viewsets import ModelViewSet
from user_account.models import User_account
from .serializers import User_accountSerializer


class  User_accountViewset(ModelViewSet):
    queryset = User_account.objects.all()
    serializer_class =  User_accountSerializer