from tutoring_session.models import TutoringSession
from tutoring_session.models import Solicitation
from tutoring_session.models import Receipt
from rest_framework import serializers

class SolicitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitation
        fields = ['status_solicitation', 'resquester', 'create_date']

class TutoringSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'name', 'subject' ,
                  'description', 'status_tutoring_session', 'create_date']

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id_receipt', 'accomplished', 'issue_date']
