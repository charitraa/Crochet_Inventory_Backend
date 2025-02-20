from rest_framework import serializers
from .models import Category , Product

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

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for view Category details.
    """
    class Meta:
        model = Category
        fields ='__all__'


class AddProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Categories create or add.
    """
    productName = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(required=True)
    class Meta:
        model = Product
        fields = ['id', 'productName','description','stock','price','category']
        

    def create(self, validated_data):
        """
         Create and return a new product with the validated data.
        """
        product = Category.objects.create(
            productName=validated_data['productName'],
            description=validated_data['description'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            category=validated_data['category']
        )
        return product
  
class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productName','description','stock','price']
        
    def update(self, instance, validated_data):
        """
          update and return instance data of products.
        """
        instance.productName = validated_data.get('productName', instance.productName)
        instance.description = validated_data.get('description', instance.description)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance