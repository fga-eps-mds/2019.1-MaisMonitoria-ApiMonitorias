from tutoring_session.models import TutoringSession
from tutoring_session.models import Solicitation
from tutoring_session.models import Receipt
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import TutoringSessionSerializer
from .serializers import SolicitationSerializer
from .serializers import ReceiptSerializer

class SolicitationViewset(ModelViewSet):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer

class TutoringSessionViewset(ModelViewSet):
    queryset = TutoringSession.objects.all()
    serializer_class = TutoringSessionSerializer

class ReceiptViewset(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer