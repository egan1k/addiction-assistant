from django.contrib.auth.base_user import BaseUserManager
from . import utils, constants


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.username = utils.generate_unique_username(user, self.model)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.account_type = constants.AccountType.admin
        user.save(using=self._db)

        return user