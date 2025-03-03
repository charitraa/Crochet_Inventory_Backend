from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for view Category details.
    """
    class Meta:
        model = Category
        fields ='__all__'


class AddCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Categories create or add.
    """
    name = serializers.CharField(required=True)
    class Meta:
        model = Category
        fields = ['id', 'name']
        

    def create(self, validated_data):
        """
         Create and return a new category with the validated data.
        """
        category = Category.objects.create(
            name=validated_data['name'],
            
        )
        return category
    
class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
    def update(self, instance, validated_data):
        """
          update and return instance data of category.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance