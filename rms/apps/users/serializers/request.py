from rest_framework import serializers
from ..models import UserModel


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'password',]


class UserRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    