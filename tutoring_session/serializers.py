from rest_framework.serializers import ModelSerializer
from tutoring_session.models import TutoringSession
from tutoring_session.models import Solicitation

class SolicitationSerializer(ModelSerializer):
    class Meta:
        model = Solicitation
        fields = ['status_solicitation', 'requester', 'create_date']

class TutoringSessionSerializer(ModelSerializer):
    #applicants = SolicitationSerializer(many=True, read_only=False)
    class Meta:
        model = TutoringSession
        fields = ['id_tutoring_session', 'name', 'subject',
                  'description', 'status_tutoring_session', 'create_date']