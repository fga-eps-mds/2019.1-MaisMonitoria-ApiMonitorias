from rest_framework.serializers import ModelSerializer
from .models import UserAccount

class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['user_account_id', 'name', 'email', 'registration_date',
                  'description', 'course', 'account_state', 'photo_url']