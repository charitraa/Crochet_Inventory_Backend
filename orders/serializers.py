from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.productName")

    class Meta:
        model = OrderItem
        fields = ["product", "product_name", "quantity", "price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user_name = serializers.ReadOnlyField(source="user.full_name")

    class Meta:
        model = Order
        fields = ["id", "user", "user_name", "order_date", "status", "total_price", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])  # Extract items data separately
        order = Order.objects.create(**validated_data)  # Create order without items

        total_price = 0  # Initialize total price

        for item in items_data:
            product = item.get("product")
            quantity = item.get("quantity")
            price = float(item.get("price"))  # Convert price from string to float

            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total_price += price * quantity  # Sum up total price

        order.total_price = total_price  # Update total price
        order.save()
        return order

    def update(self, instance, validated_data):
        """Update order and handle nested order items"""

        instance.status = validated_data.get("status", instance.status)
        instance.order_date = validated_data.get("order_date", instance.order_date)

        # Handle Order Items Update
        items_data = validated_data.pop("items", None)
        if items_data is not None:
            instance.items.all().delete()  # Delete existing items

            total_price = 0
            for item_data in items_data:
                product = item_data.get("product")
                quantity = item_data.get("quantity")
                price = float(item_data.get("price"))

                OrderItem.objects.create(order=instance, product=product, quantity=quantity, price=price)
                total_price += price * quantity

            instance.total_price = total_price  # Update total price

        instance.save()
        return instance
