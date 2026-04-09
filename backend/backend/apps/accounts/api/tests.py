from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User


class AuthenticationTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/v1/accounts/register/'
        self.login_url = '/api/v1/accounts/login/'

    def test_register_user_success(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'password_confirm': 'TestPass123!',
            'gender': 'male',
            'country': 'Saudi Arabia',
            'role': 'READER',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_password_mismatch(self):
        data = {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password': 'TestPass123!',
            'password_confirm': 'WrongPass456!',
            'role': 'READER',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_duplicate_username(self):
        User.objects.create_user(username='existing', password='pass123', is_active=True)
        data = {
            'username': 'existing',
            'email': 'new@example.com',
            'password': 'TestPass123!',
            'password_confirm': 'TestPass123!',
            'role': 'READER',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_success(self):
        User.objects.create_user(username='logintest', password='TestPass123!', is_active=True)
        response = self.client.post(self.login_url, {'username': 'logintest', 'password': 'TestPass123!'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_wrong_password(self):
        User.objects.create_user(username='logintest2', password='Correct123!', is_active=True)
        response = self.client.post(self.login_url, {'username': 'logintest2', 'password': 'Wrong123!'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile_requires_authentication(self):
        response = self.client.get('/api/v1/accounts/me/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_returns_user_data(self):
        user = User.objects.create_user(username='profiletest', password='TestPass123!', is_active=True)
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/v1/accounts/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'profiletest')

    def test_password_reset_request(self):
        User.objects.create_user(username='resettest', email='reset@example.com', password='OldPass123!', is_active=True)
        response = self.client.post('/api/v1/accounts/password-reset/', {'email': 'reset@example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)

    def test_password_reset_nonexistent_email(self):
        response = self.client.post('/api/v1/accounts/password-reset/', {'email': 'noone@example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
