from rest_framework import serializers
from .models import ribbonSize

class ribbonSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ribbonSize
        fields = ["id", "name"]