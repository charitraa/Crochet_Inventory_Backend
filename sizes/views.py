from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SizeType
from .serializers import  AddSizeTypeSerializer,SizeTypeSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

    
class SizeView(APIView):
    """ Admin view and create colors list """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
    def get(self, request, format=None):
        sizes = SizeType.objects.all()
        serializer = SizeTypeSerializer(sizes, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AddSizeTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
