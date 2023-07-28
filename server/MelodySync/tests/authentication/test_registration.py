from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class TestUserSignup(APITestCase):

    def setUp(self):
        self.url = reverse('user-list')

    def test_signup_success(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'poisson44'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().username, 'testuser')
        self.assertEqual(get_user_model().objects.get().email, 'testuser@example.com')
        self.assertTrue(check_password('poisson44', get_user_model().objects.get().password))

    def test_signup_failure_due_to_duplicate_username(self):
        get_user_model().objects.create(username='testuser', email='testuser@example.com', password='testpassword')
        data = {
            'username': 'testuser',
            'email': 'anotheruser@example.com',
            'password': 'poisson44'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['username'], ["A user with that username already exists."])

    def test_signup_failure_due_to_duplicate_email(self):
        get_user_model().objects.create(username='testuser', email='testuser@example.com', password='testpassword')
        data = {
            'username': 'anothertestuser',
            'email': 'testuser@example.com',
            'password': 'poisson44'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['email'], ["user with this email already exists."])

    def test_signup_blank_username(self):
        data = {
            'username': '',
            'email': 'testuser@example.com',
            'password': 'poisson44'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'], ["This field may not be blank."])

    def test_signup_blank_email(self):
        data = {
            'username': 'testuser',
            'email': '',
            'password': 'poisson44'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'], ["This field may not be blank."])

    def test_signup_blank_password(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'], ['This field may not be blank.'])

    def test_signup_not_valid_email(self):
        data = {
            'username': 'testuser',
            'email': 'testuser',
            'password': 'poisson44'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'], ['Enter a valid email address.'])

    def test_password_validation(self):
        data_too_short = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'po44'
        }
        response = self.client.post(self.url, data_too_short, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password'],
            ['This password is too short. It must contain at least 8 characters.']
        )

        data_too_common = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password1234'
        }
        response = self.client.post(self.url, data_too_common, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password'],
            ['This password is too common.']
        )

        data_entirely_numeric = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': '759462782156'
        }
        response = self.client.post(self.url, data_entirely_numeric, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password'],
            ['This password is entirely numeric.']
        )

        data_similar_username = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testuser1234'
        }
        response = self.client.post(self.url, data_similar_username, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password'],
            ['The password is too similar to the username.']
        )

        data_similar_email = {
            'username': 'testuser',
            'email': 'theemail@example.com',
            'password': 'theemail1234'
        }
        response = self.client.post(self.url, data_similar_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password'],
            ['The password is too similar to the email.']
        )

        data_similar_email = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'gernjgejrbgkjerkjg45643531531534564sdqggs545646546'
        }
        response = self.client.post(self.url, data_similar_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['password'],
            ['Password must be at most 24 characters long.']
        )
