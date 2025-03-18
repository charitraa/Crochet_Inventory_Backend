from rest_framework import serializers
from models import beadsType

class breadTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = beadsType
        fields = ["id", "name"]