from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
# In settings.py AUTH_USER_MODEL = 'yourapp.CustomUserModel'

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'),unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email