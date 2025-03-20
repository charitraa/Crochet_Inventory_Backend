from rest_framework import serializers
from .models import wrapperType

class wrapperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = wrapperType
        fields = ["id", "name"]