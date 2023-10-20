from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def set_password(self, raw_password):
        self.password = make_password(raw_password)