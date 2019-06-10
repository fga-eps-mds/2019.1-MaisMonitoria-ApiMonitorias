from rest_framework import serializers
from .models import UserAccount
from tutoring_session.serializers import ShortTutoringSessionSerializer
from like.serializer import GetToUserThatLikeSerializer


class ShortUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['user_account_id', 'name', 'telegram', 'photo']


class UserAccountSerializer(serializers.ModelSerializer):
    monitoring = ShortTutoringSessionSerializer(many=True, read_only=True)
    liked_tutoring_sessions = GetToUserThatLikeSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccount
        fields = ['user_account_id', 'name', 'email', 'telegram', 'registration_date',
                  'description', 'course', 'account_state', 'photo',
                  'monitoring', 'liked_tutoring_sessions']
