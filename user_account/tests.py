from rest_framework import status
from rest_framework.test import APITestCase
from .models import InterestArea
from .models import UserAccount

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


class UserAccountTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            'user_account_id': '123',
            'name': 'teste',
            'email': 'teste@gmail.com',
            'course': 'ENGENHARIAS'
        }

        self.invalid_payload = {
            'user_account_id': '',
            'name': '',
            'email': '',
            'course': ''
        }
        self.database_register = {
            "user_account_id": "123",
            "name": "teste",
            "email": "teste@gmail.com",
            "registration_date": "2019-04-25T03:22:44.599483Z",
            "description": "",
            "course": "ENGENHARIAS",
            "account_state": True,
            "photo_url": "",
            "interest_areas": [],
            "monitoring": [],
            "monitoring_history": []
        }

    def test_create_valid_user(self):
        url = '/user/'
        data = self.valid_payload
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual( UserAccount.objects.count(), 1)
        self.assertEqual(UserAccount.objects.get().user_account_id, self.database_register['user_account_id'])
        self.assertEqual(UserAccount.objects.get().name, self.database_register['name'])
        self.assertEqual(UserAccount.objects.get().email, self.database_register['email'])
        # self.assertEqual(UserAccount.objects.get().registration_date, self.database_register)
        self.assertEqual(UserAccount.objects.get().description, self.database_register['description'])
        self.assertEqual(UserAccount.objects.get().course, self.database_register['course'])
        self.assertEqual(UserAccount.objects.get().account_state, self.database_register['account_state'])
        self.assertEqual(UserAccount.objects.get().photo_url, self.database_register['photo_url'])
        # self.assertEqual(UserAccount.objects.get().interest_areas, self.database_register['interest_areas'])
        # self.assertEqual(UserAccount.objects.get().monitoring, self.database_register["monitoring"])
        # self.assertEqual(UserAccount.objects.get().monitoring_history, self.database_register["monitoring_history"])

    def test_create_invalid_user(self):
        url = '/user/'
        data = self.invalid_payload
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


