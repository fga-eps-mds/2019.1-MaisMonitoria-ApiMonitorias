from .serializers import GetTutoringSessionSerializer
from .serializers import PostTutoringSessionSerializer
from .models import TutoringSession
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter


class TutoringSessionViewset(ModelViewSet):
    queryset = TutoringSession.objects.all().order_by('-create_date')
    serializer_class = GetTutoringSessionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'subject', 'description')

    def create(self, request):
        serializer = PostTutoringSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        tutoring_session = TutoringSession.objects.latest('create_date')
        tutoring_session.monitor.monitoring.add(tutoring_session)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
