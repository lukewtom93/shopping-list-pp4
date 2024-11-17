from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Automated test for register view
class RegisterViewTests(TestCase):
    def setUp(self):
        """
        Setup tests
        """
        self.url = reverse('register')

    def unauthenticatedAccessTest(self):
        """
        Sends GET request and confirms the right
        template and access pages are used
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_list/register.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def authenticatedRedirectTest(self):
        """
        Creates a user to test the correct redirects are in place
        """
        test_user = User.objects.create_user(username='testuser',
                                             password='password')
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('shopping-list'))

    def RegistrationTest(self):
        """
        Sends a POST request to confirm the registration
        page is creating a new user
        """
        response = self.client.post(self.url, {
            'username': 'newuser',
            'password1': 'Password123',
            'password2': 'Password123',
        })

        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('shopping-list'))
