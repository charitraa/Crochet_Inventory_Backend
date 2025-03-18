from rest_framework import serializers
from models import beadsSize

class breadSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = beadsSize
        fields = ["id", "name"]