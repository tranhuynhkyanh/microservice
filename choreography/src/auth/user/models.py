from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):

    def __str__(self):
        return self.username

    @property
    def token(self):
        refresh_token = RefreshToken.for_user(self)
        return refresh_token, refresh_token.access_token
