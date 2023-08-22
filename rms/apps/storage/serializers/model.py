from rest_framework import serializers  

from ..models import StorageModel


class StorageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageModel
        fields = '__all__'
        