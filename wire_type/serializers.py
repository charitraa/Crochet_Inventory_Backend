from rest_framework import serializers
from .models import wireType

class wireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = wireType
        fields = ["id", "name"]