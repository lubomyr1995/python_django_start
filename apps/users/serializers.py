from rest_framework import serializers

from .models import UserModel


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=20)
#     age = serializers.IntegerField()
#
#     def update(self, instance: UserModel, validated_data: dict) -> UserModel:
#         for k, v in validated_data.items():
#             setattr(instance, k, v)
#         instance.save()
#         return instance
#
#     def create(self, validated_data: dict) -> UserModel:
#         return UserModel.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # fields = '__all__'
        fields = ('id', 'name', 'age')
