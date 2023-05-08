from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(null=True, default=False)
    is_seller = models.BooleanField(null=True, default=False)
