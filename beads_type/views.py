from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from models import beadsType
from serializers import breadTypeSerializer

# Create your views here.

class BeadsView(APIView):
  def get(self, request):
    beads = beadsType.objects.all()
    serializer = breadTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = breadTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

