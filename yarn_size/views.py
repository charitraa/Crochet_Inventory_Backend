from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from permissions.permissions import IsSuperuserOrAdmin, LoginRequiredPermission

from .models import yarnSize
from .serializers import yarnSizeSerializer

# Create your views here.

class YarnView(APIView):
  permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]
  
  def get(self, request):
    beads = yarnSize.objects.all()
    serializer = yarnSizeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = yarnSizeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
