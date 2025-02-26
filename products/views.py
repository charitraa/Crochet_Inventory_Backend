from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product
from .serializers import AddCategorySerializer, CategorySerializer,AddProductSerializer, ProductSerializer,CategoryUpdateSerializer,ProductUpdateSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

class CategoryView(APIView):
    """ Admin Create a new category and view it"""
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
class CategoryViewById(CategoryView):
    """ Admin view and update a category """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
    def get(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategoryUpdateSerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    def delete_category(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    
class ProductView(APIView):
    """ Admin view and create product list """
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
    

    
class ProductViewById(ProductView):
    """ Admin view and update a product """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
    def get(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductUpdateSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    