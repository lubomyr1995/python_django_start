from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_image_for_profile import upload_to

from .menagers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,
                                validators=[V.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.message)])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)])
    surname = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)])
    age = models.IntegerField(validators=[V.MinValueValidator(18), V.MaxValueValidator(150)])
    phone = models.CharField(max_length=10, validators=[V.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.message)])
    avatar = models.ImageField(upload_to=upload_to, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
