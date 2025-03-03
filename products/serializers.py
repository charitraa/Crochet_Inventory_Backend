from rest_framework import serializers
from .models import Product
    
class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for view Products details.
    """
    class Meta:
        model = Product
        fields ='__all__'


class AddProductSerializer(serializers.ModelSerializer):
    """
    Serializer for products create or add.
    """
    productName = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = Product
        fields = ['id', 'productName','description','stock','price','category','image']
        

    def create(self, validated_data):
        """
         Create and return a new product with the validated data.
        """
        product = Product.objects.create(
            productName=validated_data['productName'],
            description=validated_data['description'],
            price=validated_data['price'],
            stock=validated_data['stock'],
            image = validated_data['image'],
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