from django.db import models
from django.conf import settings


class Post(models.Model):
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
