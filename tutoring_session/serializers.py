from tutoring_session.models import TutoringSession
from rest_framework import serializers


def get_monitor_serializer():
    from user_account.serializers import ShortUserAccountSerializer
    return ShortUserAccountSerializer(many=False, read_only=True)


class ShortTutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'name', 'subject' ,
                  'description', 'status_tutoring_session', 'create_date']


class PostTutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name', 'subject' ,
                  'description', 'status_tutoring_session', 'create_date']    


class GetTutoringSessionSerializer(serializers.ModelSerializer):
    monitor = get_monitor_serializer()

    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name', 'subject' ,
                  'description', 'status_tutoring_session', 'create_date']    


