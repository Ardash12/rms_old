from rest_framework import serializers
from ..models import StorageModel


class StorageCreationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageModel
        fields = "__all__"
        read_only_fields = ["user"]
        