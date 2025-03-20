from rest_framework import serializers
from .models import PurchaseMaterial

class PurchaseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseMaterial
        fields = ['id', 'material', 'quantity', 'price', 'color', 'size', 'date']

    def create(self, validated_data):
        material = validated_data.get("material")
        color = validated_data.get("color")
        size = validated_data.get("size")
        quantity = validated_data.get("quantity")
        price = validated_data.get("price")

        # Check if material with the same color & size exists
        existing_purchase = PurchaseMaterial.objects.filter(
            material=material, color=color, size=size
        ).first()

        if existing_purchase:
            # Update quantity & price
            existing_purchase.quantity += quantity
            existing_purchase.price += price
            existing_purchase.save()
            return existing_purchase
        else:
            # Create new entry
            return super().create(validated_data)
