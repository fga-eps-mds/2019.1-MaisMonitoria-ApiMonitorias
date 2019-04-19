from rest_framework.serializers import ModelSerializer
from monitoring.models import Monitoring

class MonitoringSerializer(ModelSerializer):
    class Meta:
        model = Monitoring
        fields = ['id_monitoring', 'name_monitoring', 'matter',
                  'description', 'status_monitoring', 'create_date']