from rest_framework.serializers import ModelSerializer, ImageField
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_account

class UserSerializer(ModelSerializer):
    class Meta:
        model = User_account
        fields = ('user_account_id', 'name', 'email')