from rest_framework.serializers import ModelSerializer
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(**validated_data)
        try:
            validate_password(validated_data['password'], user=user)

        except exceptions.ValidationError as e:
            raise exceptions.ValidationError({'password': e.messages})

        user.set_password(validated_data['password'])
        user.save()
        return user
