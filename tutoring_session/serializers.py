from tutoring_session.models import TutoringSession
from rest_framework import serializers
from like.serializer import GetToTutoringSessionLikeSerializer


def get_serializer():
    from user_account.serializers import ShortUserAccountSerializer
    return ShortUserAccountSerializer(many=False, read_only=True)


class ShortTutoringSessionSerializer(serializers.ModelSerializer):
    likes = GetToTutoringSessionLikeSerializer(many=True, read_only=True)

    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'name', 'subject' ,
                  'description', 'status_tutoring_session', 
                  'likes', 'total_likes', 'create_date']


class PostTutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name',
                  'subject', 'description', 'create_date']    


class GetTutoringSessionSerializer(serializers.ModelSerializer):
    likes = GetToTutoringSessionLikeSerializer(many=True, read_only=True)
    monitor = get_serializer()

    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name', 
                  'subject', 'description', 'status_tutoring_session',
                  'create_date', 'likes', 'total_likes']    



