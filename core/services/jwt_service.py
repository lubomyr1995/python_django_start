from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from core.enums.action_token_enum import ActionEnum
from core.exceptions.jwt_exception import JWTException

from apps.users.models import UserModel as User

UserModel: User = get_user_model()

ActionTokenClassType = Type[BlacklistMixin | Token]


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.lifetime
    token_type = ActionEnum.ACTIVATE.token_type


class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenClassType):
        try:
            activate_token = token_class(token)
            activate_token.check_blacklist()
        except Exception:
            raise JWTException
        activate_token.blacklist()
        user_id = activate_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
        # get_object_or_404 -- повертає юзера якщо все добре
