from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from permissions.permissions import IsSuperuserOrAdmin, LoginRequiredPermission

from .models import wireSize
from .serializers import wireSizeSerializer

# Create your views here.

class WireView(APIView):
  permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
  
  def get(self, request):
    beads = wireSize.objects.all()
    serializer = wireSizeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = wireSizeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
class WireSizeDeleteView(APIView):
  def delete(self, request, pk):
    wire = wireSize.objects.get(pk=pk)
    wire.delete()
    return Response(status=204)
  