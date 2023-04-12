import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.enums.template_enum import TemplateEnum
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject: str = ''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register_email(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'{os.environ.get("FRONTEND_URL")}/activate/{token}'
        cls.__send_email(user.email, TemplateEnum.REGISTER.template_name, {'name': user.profile.name, 'url': url},
                         TemplateEnum.REGISTER.name_subject)

    @classmethod
    def recovery_password(cls, user):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'{os.environ.get("FRONTEND_URL")}/recovery_password/{token}'
        cls.__send_email(user.email, TemplateEnum.RECOVERY.template_name, {'name': user.profile.name, 'link': url},
                         TemplateEnum.RECOVERY.name_subject)
