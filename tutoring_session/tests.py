from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TutoringSession

# from rest_framework.status import (
#     HTTP_403_FORBIDDEN,
#     HTTP_200_OK,
#     HTTP_404_NOT_FOUND,
#     HTTP_400_BAD_REQUEST,
#     HTTP_500_INTERNAL_SERVER_ERROR
# )


class TutoringSessionTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'teste'
            # 'monitor': 'adsfg'
            # 'name': 'test'
            # 'subject': 'teste'            
        }

        self.invalid_payload = {
            'name': ''            
        }

    
    # def test_create_valid_tutoring(self):
    #     url = '/tutoring/'
    #     data = self.valid_payload
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(TutoringSession.objects.count(), 1)
    #     # self.assertEqual(Tutoring.objects.get().name, self.valid_payload['name'])
    #     # self.assertEqual(Tutoring.objects.get().monitor, self.valid_payload['monitor'])
    #     self.assertEqual(TutoringSession.objects.get().name, self.valid_payload['name'])
    #     # self.assertEqual(Tutoring.objects.get().subject, self.valid_payload['subject'])


    def test_create_invalid_tutoring(self):
        url = '/tutoring/'
        data = self.invalid_payload
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)