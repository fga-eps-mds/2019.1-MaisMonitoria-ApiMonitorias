from rest_framework.serializers import ModelSerializer
from user_account.models import User_account


class User_accountSerializer(ModelSerializer):
    class Meta:
        model = User_account
        fields = ['user_account_id','name','email','registration_date', 'description','course','account_state', 'photo_url']