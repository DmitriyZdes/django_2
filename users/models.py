from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=50, verbose_name='номер телефона', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)
    is_verified = models.BooleanField(default=True, verbose_name='верифицирован ли аккаунт')
    verify_code = models.CharField(default=0, verbose_name='код верификации', max_length=100)
