from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model


class TestUserLogin(APITestCase):

	# Don't instantiate a new user for each test
	@classmethod
	def setUpTestData(cls):
		User = get_user_model()
		cls.url = reverse('user-login')
		cls.username = 'testuser'
		cls.password = 'poisson44'
		cls.user = User.objects.create_user(
			username=cls.username,
			email='testuser@email.com',
			password=cls.password
		)

	def setUp(self):
		self.client = APIClient()

	def test_login_success(self):
		data = {
			'username': self.username,
			'password': self.password
		}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['status'], 'login successful')

	def test_login_session(self):
		data = {
			'username': self.username,
			'password': self.password
		}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(self.client.session['username'], 'testuser')
		self.assertIn('sessionid', response.cookies)
		self.assertIn('csrftoken', response.cookies)
		self.assertEqual(response.cookies['sessionid']['expires'], '')
		self.assertEqual(self.client.session.get_expiry_age(), 7200)

	def test_stay_connected_True(self):
		data = {
			'username': self.username,
			'password': self.password,
			'stay_connected': True
		}
		response = self.client.post(self.url, data, format='json')
		self.assertIn('sessionid', response.cookies)
		self.assertIsNotNone(response.cookies['sessionid']['expires'])
		# Check if the session lasts for 90 days
		self.assertEqual(self.client.session.get_expiry_age(), 7776000)

	def test_login_failure(self):
		data = {
			'username': 'wrongusername',
			'password': 'wrongpassword'
		}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
		self.assertEqual(response.data['error'], 'Invalid Credentials')

	def test_login_missing_credentials(self):
		data = {
			'username': self.username
		}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data['error'], 'Missing Credentials')

	def test_login_case_sensitive_username(self):
		data = {
			'username': self.username.upper(),
			'password': self.password
		}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
		self.assertEqual(response.data['error'], 'Invalid Credentials')
