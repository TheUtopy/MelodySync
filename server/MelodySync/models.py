from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    last_name = None
    first_name = None
    email = models.EmailField(max_length=100, unique=True)
    date_updated = models.DateTimeField(auto_now_add=True)
