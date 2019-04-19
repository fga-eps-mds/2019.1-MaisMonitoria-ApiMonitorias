from rest_framework.viewsets import ModelViewSet
from monitoring.models import Monitoring
from .serializers import MonitoringSerializer

class MonitoringViewset(ModelViewSet):
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer


