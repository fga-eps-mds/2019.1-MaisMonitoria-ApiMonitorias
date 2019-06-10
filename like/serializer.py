from rest_framework import serializers
from .models import Like

from user_account.models import UserAccount
from tutoring_session.models import TutoringSession


class ShortUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['user_account_id', 'name', 'photo']


class GetToTutoringSessionLikeSerializer(serializers.ModelSerializer):
    user_that_likes = ShortUserAccountSerializer(many=False, read_only=True)

    class Meta:
        model = Like
        fields = ['id_like', 'user_that_likes', 'create_date']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class GetTutoringSessionSerializer(serializers.ModelSerializer):
    likes = GetToTutoringSessionLikeSerializer(many=True, read_only=True)
    monitor = ShortUserAccountSerializer(many=False, read_only=True)

    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name',
                  'subject', 'description', 'status_tutoring_session',
                  'create_date', 'likes', 'total_likes']


class GetToUserThatLikeSerializer(serializers.ModelSerializer):
    tutoring_session = GetTutoringSessionSerializer(many=False, read_only=True)

    class Meta:
        model = Like
        fields = ['id_like', 'tutoring_session', 'create_date']
