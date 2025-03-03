from rest_framework import serializers
from .models import Material

class MaterialSerializer(serializers.ModelSerializer):
    """
    Serializer for view Material details.
    """
    class Meta:
        model = Material
        fields ='__all__'


class AddMaterialSerializer(serializers.ModelSerializer):
    """
    Serializer for Categories create or add.
    """
    name = serializers.CharField(required=True)
    class Meta:
        model = Material
        fields = ['id', 'name']
        

    def create(self, validated_data):
        """
         Create and return a new Material with the validated data.
        """
        Material = Material.objects.create(
            name=validated_data['name'],
            
        )
        return Material
    
class MaterialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']
        
    def update(self, instance, validated_data):
        """
          update and return instance data of Material.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance