from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .views import TutoringSessionViewset
from user_account.models import UserAccount
from .models import TutoringSession


class TutoringSessionViewsetTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'monitor': '211297',
            'name': 'encapsulamento',
            'subject': 'Orientação a Objetos',
            
        }

        self.invalid_payload = {
            'name': ''            
        }
       
    def test_create_valid_tutoring(self):
        user = UserAccount(name='moacir', user_account_id="211297", 
                           email='moacir@moacir', course='AERO')
        user.save()
        url = '/tutoring/'
        data = self.valid_payload
        response = self.client.post(url, data, format='json')
        tutoring_session = TutoringSession.objects.latest('create_date')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tutoring_session in user.monitoring.all(), True)

    def test_create_invalid_tutoring(self):
        url = '/tutoring/'
        data = self.invalid_payload
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)