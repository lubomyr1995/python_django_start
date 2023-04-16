from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class SwaggerUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'id', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile'
        )


class SwaggerTokenObtainPairAndUserSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    user = SwaggerUserSerializer()
