from tutoring_session.models import TutoringSession
from tutoring_session.models import Solicitation
from tutoring_session.models import Receipt
from rest_framework import serializers


def get_monitor_serializer():
    from user_account.serializers import ShortUserAccountSerializer
    return ShortUserAccountSerializer(many=False, read_only=True)


class SolicitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = ['status_solicitation', 'resquester', 'create_date']


class ShortTutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'name', 'subject' , 'applicants',
                  'description', 'status_tutoring_session', 'create_date', 
                  'accepted_applicants']


class PostTutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name', 'subject' ,'applicants',
                  'description', 'status_tutoring_session', 'create_date','accepted_applicants']    


class GetTutoringSessionSerializer(serializers.ModelSerializer):
    monitor = get_monitor_serializer()

    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'monitor', 'name', 'subject' ,'applicants',
                  'description', 'status_tutoring_session', 'create_date','accepted_applicants']    


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id_receipt', 'accomplished', 'issue_date']
