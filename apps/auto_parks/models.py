from django.db import models
from django.core import validators as V
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

from core.enums.regex_enum import RegEx

UserModel: User = get_user_model()


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)])
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
