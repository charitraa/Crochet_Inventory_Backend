from rest_framework import serializers
from .models import yarnSize

class yarnSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = yarnSize
        fields = ["id", "name"]