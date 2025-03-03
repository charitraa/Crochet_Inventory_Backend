from rest_framework import serializers
from .models import ColorType

class ColorTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for view Color details.
    """
    class Meta:
        model = ColorType
        fields ='__all__'


class AddColorSerializer(serializers.ModelSerializer):
    """
    Serializer for Color.
    """
    name = serializers.CharField(required=True)
    class Meta:
        model = ColorType
        fields = ['id', 'name']
        

    def create(self, validated_data):
        """
         Create and return a new color with the validated data.
        """
        color = ColorType.objects.create(
            name=validated_data['name'],
            
        )
        return color
    
# class CategoryUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']
        
#     def update(self, instance, validated_data):
#         """
#           update and return instance data of category.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance