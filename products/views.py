from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product
from .serializers import AddCategorySerializer, CategorySerializer,AddProductSerializer, ProductSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

class CategoryView(APIView):
    """ Admin Create a new user"""
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]

    def post(self, request, format=None):
        serializer = AddCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProductView(APIView):
    """ Admin view a product list """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AddProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)