from django.shortcuts import get_object_or_404
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from crochet_inventory_system import settings
from permissions.permissions import LoginRequiredPermission
from .models import Order
from .serializers import OrderSerializer

class OrderAPIView(APIView):
    permission_classes = [LoginRequiredPermission]

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

class OrderApiViewById(APIView):
    permission_classes = [LoginRequiredPermission]

    
    def get(self, request, pk, format=None):
        """Fetch an order by its ID"""
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update an existing order"""
        order = get_object_or_404(Order, pk=pk)  # Ensure the order exists
        serializer = OrderSerializer(order, data=request.data, partial=True)  # Allow partial updates

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete an existing order"""
        order = get_object_or_404(Order, pk=pk)  # Ensure the order exists
        order.delete()
        return Response({"message": "Order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)