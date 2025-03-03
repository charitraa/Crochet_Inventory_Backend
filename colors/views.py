from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ColorType
from .serializers import  ColorTypeSerializer,AddColorSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

    
class ColorView(APIView):
    """ Admin view and create colors list """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
    def get(self, request, format=None):
        colors = ColorType.objects.all()
        serializer = ColorTypeSerializer(colors, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AddColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)