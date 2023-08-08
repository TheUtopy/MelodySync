from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class ContactView(APIView):

    def post(self, request):
        email = request.data.get('email')
        message = request.data.get('message')

        if not email or not message or message == 'Your message goes here.':
            return Response({'error': 'Email and/or message fields are empty.'}, status=status.HTTP_400_BAD_REQUEST)

        if len(message) > 500:
            return Response({'error': 'Message is too long. Must be 500 charracters max.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)

            send_mail(
                subject=f'Message from {email} via MelodySync Contact form',
                message=message,
                from_email=email,
                recipient_list=['admin@MelodySync.xyz']
            )

            return Response({'Success': 'Email sent'}, status=status.HTTP_200_OK)

        except ValidationError as e:
            print(e)
            response_data = {'error' : e.messages[0]}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


