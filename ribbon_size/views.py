from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ribbonSize
from .serializers import ribbonSizeSerializer

# Create your views here.

class RibbonView(APIView):
  def get(self, request):
    beads = ribbonSize.objects.all()
    serializer = ribbonSizeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = ribbonSizeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
