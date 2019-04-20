from rest_framework import serializers
from .models import UserAccount
from .models import InterestArea

class UserAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['user_account_id', 'name', 'email', 'registration_date',
                  'description', 'course', 'account_state', 'photo_url','interest_areas']

class InterestAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterestArea
        fields = ['id_interest_area','name']