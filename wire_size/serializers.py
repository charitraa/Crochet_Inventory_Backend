from rest_framework import serializers
from .models import wireSize

class wireSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = wireSize
        fields = ["id", "name"]