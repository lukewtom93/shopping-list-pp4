from django.test import TestCase
from django.contrib.auth.models import User
from shopping_list.models import ShoppingList


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

    def test_user_logout(self):
        User.objects.create_user(username='testuser', password='StrongPass123')
        self.client.login(username='testuser', password='StrongPass123')
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)


class ItemTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='StrongPass123')
        self.client.login(username='testuser', password='StrongPass123')

    def test_create_item(self):
        response = self.client.post('/add/', {'title': 'Milk'})
        self.assertEqual(response.status_code, 404)
        self.assertFalse(ShoppingList.objects.filter(title='Milk', user=self.user).exists())

    def test_delete_item(self):
        item = ShoppingList.objects.create(title='Bread', user=self.user)
        response = self.client.post(f'/delete/{item.id}/')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(ShoppingList.objects.filter(id=item.id).exists())

    def test_cross_off_item(self):
        item = ShoppingList.objects.create(title='Eggs', user=self.user)
        response = self.client.post(f'/cross_off/{item.id}/')
        self.assertEqual(response.status_code, 404)
        item.refresh_from_db()
        self.assertFalse(item.complete)