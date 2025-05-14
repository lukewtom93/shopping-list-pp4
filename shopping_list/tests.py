from django.test import TestCase
from django.contrib.auth.models import User


class AuthenticationTests(TestCase):
    def test_user_registration(self):
        response = self.client.post('/register/', {
            'username': 'testuser',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='StrongPass123')
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'StrongPass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)