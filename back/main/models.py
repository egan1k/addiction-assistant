from django.contrib.auth.models import AbstractUser
from django.db import models

from . import constants, managers


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    account_type = models.CharField(
        choices=constants.AccountType.choices,
        default=constants.AccountType.regular_user,
        max_length=20,
    )
    objects = managers.CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
