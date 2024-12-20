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
    is_locked = models.BooleanField(default=False)
    locked_until = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(
        choices=constants.AccountType.choices,
        default=constants.AccountType.regular_user,
        max_length=20,
    )
    login_attempts_left = models.PositiveSmallIntegerField(
        blank=True, null=True, default=5
    )
    last_failed_login_attempt = models.DateTimeField(blank=True, null=True)

    objects = managers.CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
