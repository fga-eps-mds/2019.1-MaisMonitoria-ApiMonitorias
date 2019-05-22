from .serializers import GetTutoringSessionSerializer, SolicitationSerializer
from .serializers import ReceiptSerializer, PostTutoringSessionSerializer
from tutoring_session.models import TutoringSession, Solicitation, Receipt
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from user_account.models import UserAccount
from rest_framework import status
from rest_framework.filters import SearchFilter


class SolicitationViewset(ModelViewSet):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer


class TutoringSessionViewset(ModelViewSet):
    queryset = TutoringSession.objects.all()
    serializer_class = GetTutoringSessionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'subject','description')

    def create(self, request):
        serializer = PostTutoringSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        tutoring_session = TutoringSession.objects.latest('create_date')
        tutoring_session.monitor.monitoring.add(tutoring_session)        

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReceiptViewset(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

