from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Object, Picture


class ObjSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    Picture = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Object
        fields = ['id', 'name', 'description', 'Picture', 'owner']


class UserSerializer(serializers.ModelSerializer):
    object = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'object']


class PictureSerializer(serializers.ModelSerializer):
    obj=serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())

    class Meta:
        model = Picture
        fields = ['id', 'name', 'image', 'obj']


"""class PictureSerializer(serializers.ModelSerializer):
    object_name = serializers.ReadOnlyField(source='obj.name')
    owner = serializers.ReadOnlyField(source='obj.owner.username')
    description = serializers.ReadOnlyField(source='obj.description')

    class Meta:
        model = Picture
        fields = ['id', 'name', 'image', 'object_name', 'description', 'owner']
"""
