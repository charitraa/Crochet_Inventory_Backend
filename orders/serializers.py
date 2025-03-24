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
            # Extract items from request data
            items_data = validated_data.pop("items", [])

            # Update other order fields
            instance.user = validated_data.get("user", instance.user)
            instance.total_price = validated_data.get("total_price", instance.total_price)
            instance.save()

            # Update or create items
            existing_items = {item.product.id: item for item in instance.items.all()}  # Get existing items

            for item_data in items_data:
                product = item_data.get("product")
                quantity = item_data.get("quantity", 1)
                price = float(item_data.get("price", 0))

                if product.id in existing_items:
                    # Update existing item
                    order_item = existing_items[product.id]
                    order_item.quantity = quantity
                    order_item.price = price
                    order_item.save()
                else:
                    # Create new item
                    OrderItem.objects.create(order=instance, product=product, quantity=quantity, price=price)

            # Recalculate total price
            instance.total_price = sum(item.price * item.quantity for item in instance.items.all())
            instance.save()

            return instance