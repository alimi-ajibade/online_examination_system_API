from distutils.command.upload import upload
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]
