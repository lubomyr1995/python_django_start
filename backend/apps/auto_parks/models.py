from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_image_for_autopark import upload_to

from apps.auto_parks.managers import AutoParkManager
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)])
    image = models.ImageField(upload_to=upload_to, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')

    objects = AutoParkManager.as_manager()

    def __str__(self):
        return self.name


class ChatModel(models.Model):
    class Meta:
        db_table = 'chat'
        ordering = ['id']

    message = models.CharField(max_length=255)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
