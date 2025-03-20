from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import glueType
from .serializers import glueTypeSerializer

# Create your views here.

class glueView(APIView):
  def get(self, request):
    beads = glueType.objects.all()
    serializer = glueTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = glueTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

