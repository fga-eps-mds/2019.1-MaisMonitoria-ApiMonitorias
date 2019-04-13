from rest_framework.serializers import ModelSerializer
from user_account.models import User_account

class User_account_Serializer(ModelSerializer):
    class Meta:
        model = User_account
        fields = ['user_account_id', 'name', 'description', 'course']