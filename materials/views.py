from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Material
from .serializers import AddMaterialSerializer, MaterialSerializer, MaterialUpdateSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

class MaterialView(APIView):
    """ Admin Create a new Material and view it """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]

    def post(self, request, format=None):
        serializer = AddMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)
    
class MaterialViewById(MaterialView):
    """ Admin view and update a Material """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
    def get(self, request, pk, format=None):
        try:
            material = Material.objects.get(pk=pk)
            serializer = MaterialSerializer(material)
            return Response(serializer.data)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, format=None):
        try:
            material = Material.objects.get(pk=pk)
            serializer = MaterialUpdateSerializer(material, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk, format=None):
        try:
            material = Material.objects.get(pk=pk)
            material.delete()
            return Response({"message": "Material deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)
    