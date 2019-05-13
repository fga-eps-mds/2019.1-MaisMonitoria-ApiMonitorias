from rest_framework import serializers
from tutoring_session.serializers import TutoringSessionSerializer
from .models import UserAccount
from .models import InterestArea

class UserAccountSerializer(serializers.ModelSerializer):
    monitoring = TutoringSessionSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccount
        fields = ['user_account_id', 'name', 'email', 'registration_date',
                  'description', 'course', 'account_state', 'photo_url','interest_areas','monitoring','monitoring_history']

class InterestAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestArea
        fields = ['id_interest_area','name']