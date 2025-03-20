from rest_framework import serializers
from .models import yarnType

class yarnTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = yarnType
        fields = ["id", "name"]