from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from regist.validators import username_validator, image_validator, password_validator


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, validators=[username_validator])
    image = models.ImageField(upload_to='user_images/', validators=[image_validator])
    password = models.CharField(max_length=32, validators=[password_validator])
    birthdate = models.DateField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
