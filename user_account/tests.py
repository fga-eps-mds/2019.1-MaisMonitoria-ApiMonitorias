from rest_framework import status
from rest_framework.test import APITestCase
from .models import InterestArea

# Create your tests here.

class InterestAreaTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'teste'
        }

        self.invalid_payload = {
            'name': ''
        }

    def test_create_valid_interest_area(self):
        url = '/interestarea/'
        data = self.valid_payload
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InterestArea.objects.count(), 1)
        self.assertEqual(InterestArea.objects.get().name, self.valid_payload['name'])

    def test_create_invalid_interest_area(self):
        url = '/interestarea/'
        data = self.invalid_payload
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



