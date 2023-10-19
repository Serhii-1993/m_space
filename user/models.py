from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=10, blank=True, unique=True)
    #
    #
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    # is_anonymous = True
    # is_authenticated = False
    pass