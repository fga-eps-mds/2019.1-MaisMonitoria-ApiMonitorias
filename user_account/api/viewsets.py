from rest_framework.viewsets import ModelViewSet
from user_account.models import User_account
from .serializers import User_account_Serializer

class User_account_ViewSet(ModelViewSet):
    queryset = User_account.objects.all()
    serializers_class = User_account_Serializer
