from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your tests here.

class RegisterViewTests(TestCase):
    def setUp(self):
        self.url = reverse('register')

    def unauthenticatedAccessTest (self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_list/register.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def authenticatedRedirectTest(self):
        test_user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('shopping-list'))

    def RegistrationTest(self):
        response = self.client.post(self.url, {
            'username': 'newuser',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123',
        })

  
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('shopping-list'))
