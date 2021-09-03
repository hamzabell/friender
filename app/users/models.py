from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email must be set'))

        email = self.normalize_email(email)

        instance = self.model(email=email, **extra_fields)
        instance.set_password(password)

        instance.save()

        return instance

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is_superuser must be set to True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('is_staff must be set to True'))

        return self.create_user(email, password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.TextField()
    date_of_birth = models.DateField(auto_now=False, null=True)
    avatar = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects= UserManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

