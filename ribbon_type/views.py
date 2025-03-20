from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ribbonType
from .serializers import ribbonTypeSerializer

# Create your views here.

class ribbonView(APIView):
  def get(self, request):
    beads = ribbonType.objects.all()
    serializer = ribbonTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = ribbonTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

