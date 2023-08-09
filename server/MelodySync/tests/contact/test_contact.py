from django.urls import reverse
from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase


class TestContactForm(APITestCase):

    def setUp(self):
        self.url = reverse('contact')
        self.email = "test@test.com"
        self.message = "This is a message for the test"
        self.data = {
            "email": self.email,
            "message": self.message
        }

    def test_contact_response_ok(self):
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "Success": "Email sent"
        })

    def test_email_received(self):
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, f'Message from {self.email} via MelodySync Contact form')
        self.assertEqual(mail.outbox[0].body, self.message)
        self.assertEqual(mail.outbox[0].from_email, self.email)
        self.assertEqual(mail.outbox[0].to, ['admin@MelodySync.xyz'])

    def test_email_empty(self):
        data = {
            "email": "",
            "message": self.message
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "error": "Email and/or message fields are empty."
        })

    def test_message_empty_or_default(self):
        data_empty = {
            "email": self.email,
            "message": ""
        }
        response = self.client.post(self.url, data_empty, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "error": "Email and/or message fields are empty."
        })

        data_default = {
            'email': self.email,
            'message': 'Your message goes here.'
        }
        response = self.client.post(self.url, data_default, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "error": "Email and/or message fields are empty."
        })

    def test_message_too_long(self):
        data = {
            "email": self.email,
            "message": "This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. This message is way too long. "
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "error": "Message is too long. Must be 500 characters max."
        })

    def test_not_valid_email(self):
        data = {
            "email": "email",
            "message": self.message
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "error": "Enter a valid email address."
        })

