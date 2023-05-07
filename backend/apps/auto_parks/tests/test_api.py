from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.auto_parks.models import AutoParkModel
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AutoParkTestCase(APITestCase):
    def _authenticate(self):
        email = 'user@gmail.com'
        password = 'P@$$word1'
        self.client.post(reverse('v1:auth_register'), {
            "email": email,
            "password": password,
            "profile": {
                "name": "Homer",
                "surname": "Simpson",
                "age": 40,
                "phone": "0997274502"
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        response = self.client.post(reverse('v1:auth_login'), {"email": email, "password": password})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_create_auto_park_without_auth(self):
        count = AutoParkModel.objects.count()
        auto_park = {
            'name': 'Uklon'
        }
        response = self.client.post(reverse('v1:auto_park_list_create'), auto_park)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(AutoParkModel.objects.count(), count)

    def create_auto_park(self):
        self._authenticate()
        count = AutoParkModel.objects.count()
        auto_park = {
            'name': 'Uklon'
        }
        response = self.client.post(reverse('v1:auto_park_list_create'), auto_park)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data['name'], 'Uklon')
        self.assertIsInstance(response.data['cars'], list)
        self.assertEquals(AutoParkModel.objects.count(), count + 1)
