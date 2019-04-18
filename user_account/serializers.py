from rest_framework import serializers
from .models import User_account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_account
        fields = ('user_account_id', 'course', 'description', 'registration_date', 'account_state')