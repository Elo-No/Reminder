from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.account.enums import GenderStatus
from apps.core.models import BaseModel

from utils.validatoin_phone import phone_number_validation

class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, phone_number, password=None):
        if not username:
            raise ValueError('Users must have username')
        if not first_name:
            raise ValueError('Users must have first name')
        if not last_name:
            raise ValueError('Users must have last name')
        if not phone_number:
            raise ValueError('Users must have a mobile number')
        if not phone_number_validation(phone_number):
            raise ValueError('Invalid mobile number')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, phone_number, password=None):
        if not username:
            raise ValueError('Users must have username')
        if not first_name:
            raise ValueError('Users must have first name')
        if not last_name:
            raise ValueError('Users must have last name')
        if not phone_number:
            raise ValueError('Users must have a mobile number')
        if not phone_number_validation(phone_number):
            raise ValueError('Invalid mobile number')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            is_superuser=True,
            is_staff=True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, BaseModel):
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=32,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=64,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=64,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        max_length=32,
        unique=True,
    )
    gender = models.IntegerField(
        choices = GenderStatus.choices,default= GenderStatus.NONE
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"({self.first_name} - {self.last_name} - {self.mobile_number})"
