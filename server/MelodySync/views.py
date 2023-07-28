from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError as DjangoValidationError


from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)

        except DRFValidationError as e:
            not_unique_username = "username" in e.get_codes() and e.get_codes()["username"] == ["unique"]
            not_unique_email = "email" in e.get_codes() and e.get_codes()["email"] == ["unique"]
            if not_unique_username or not_unique_email:
                return Response(e.detail, status=status.HTTP_409_CONFLICT)

            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except DjangoValidationError as e:
            return Response({'password': e.messages}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return Response({'status': 'login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
