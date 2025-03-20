from rest_framework import serializers
from .models import keyringType

class keyringTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = keyringType
        fields = ["id", "name"]