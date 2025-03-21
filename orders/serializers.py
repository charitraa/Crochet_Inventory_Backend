from rest_framework import serializers

from products.models import Product
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.productName")
    class Meta:
        model = OrderItem
        fields = ["product","product_name","quantity","price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user_name = serializers.ReadOnlyField(source="user.full_name")

    class Meta:
        model = Order
        fields = ["id", "user","user_name", "order_date", "status", "total_price", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")  # Extract items data separately
        order = Order.objects.create(**validated_data)  # Create order without items

        total_price = 0  # Initialize total price

        for item in items_data:
            print(items_data)
            product = item.get("product")  # Correct field name from frontend
            if not product:
                raise serializers.ValidationError({"product": "This field is required."})
            quantity = item.get("quantity")
            if not quantity:
                raise serializers.ValidationError({"quantity": "This field is required."})

            price = float(item.get("price"))  # Convert price from string to float
            # Create order item
# Create order item
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total_price += price * quantity  # Sum up total price

        order.total_price = total_price  # Update total price
        order.save()
        return order
