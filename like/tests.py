from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .views import LikeViewSet
from .models import Like
from tutoring_session.models import TutoringSession
from user_account.models import UserAccount


class LikeTests(APITestCase):
    def setUp(self):
        self.valid_payload = {
            
            'user_that_likes':'2',
            'tutoring_session':'1',
        }

        self.invalid_payload = {
            'id_like': ''            
        }
    def test_create_like(self):
        user1= UserAccount(name='moacir', user_account_id="1", 
                           email='moacir@moacir', course='AERO')
        user1.save()                   
        tutoring = TutoringSession(monitor=user1,name='derivada', subject='c1')
        tutoring.save()
        user2=UserAccount(name='moacir', user_account_id="2", 
                           email='moacir@moacir', course='AERO')
        user2.save()
        url = '/like/'
        data = self.valid_payload
        response = self.client.post(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(Like.objects.get().id_like, 1)

    def test_delete_like(self):
        user1= UserAccount(name='moacir', user_account_id="1", 
                           email='moacir@moacir', course='AERO')
        user1.save()                   
        tutoring = TutoringSession(monitor=user1,name='derivada', subject='c1')
        tutoring.save()
        user2=UserAccount(name='moacir', user_account_id="2", 
                           email='moacir@moacir', course='AERO')
        user2.save()
        like= Like(user_that_likes=user2,tutoring_session = tutoring )
        like.save()
        
        data = {'id_like':2}
        url= '/like/'+str(data['id_like'])+'/'
        
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Like.objects.count(), 0)
        

    