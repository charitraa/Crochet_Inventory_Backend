from rest_framework import serializers
from .models import ribbonType

class ribbonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ribbonType
        fields = ["id", "name"]