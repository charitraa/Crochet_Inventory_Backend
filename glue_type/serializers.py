from rest_framework import serializers
from .models import glueType

class glueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = glueType
        fields = ["id", "name"]