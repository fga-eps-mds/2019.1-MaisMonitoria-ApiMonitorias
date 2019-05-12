from tutoring_session.models import TutoringSession
from tutoring_session.models import Solicitation
from tutoring_session.models import Receipt
from rest_framework import serializers

class SolicitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = ['status_solicitation', 'resquester', 'create_date']

class TutoringSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['monitor','id_tutoring_session', 'name', 'subject' ,'applicants',
                  'description', 'status_tutoring_session', 'create_date','accepted_applicants']

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id_receipt', 'accomplished', 'issue_date']
