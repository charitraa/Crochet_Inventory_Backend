import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from crochet_inventory_system import settings
from .models import Order
from .serializers import OrderSerializer

class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """Fetch all orders"""
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Create a new order and assign it to the logged-in user"""
             
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save order with user ID
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        