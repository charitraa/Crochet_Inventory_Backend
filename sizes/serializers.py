from rest_framework import serializers
from .models import SizeType

class SizeTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for view sizes details.
    """
    class Meta:
        model = SizeType
        fields ='__all__'


class AddSizeTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for sizes.
    """
    name = serializers.CharField(required=True)
    class Meta:
        model = SizeType
        fields = ['id', 'name']
        

    def create(self, validated_data):
        """
         Create and return a new sizes with the validated data.
        """
        color = SizeType.objects.create(
            name=validated_data['name'],
        )
        return color
