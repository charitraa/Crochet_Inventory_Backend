from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import AddCategorySerializer, CategorySerializer,CategoryUpdateSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

class CategoryView(APIView):
    """ Admin Create a new category and view it"""
    permission_classes = [LoginRequiredPermission]

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
    def delete(self, request, pk, format=None):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    