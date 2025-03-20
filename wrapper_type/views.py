from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import wrapperType
from .serializers import wrapperTypeSerializer

# Create your views here.

class wrapperView(APIView):
  def get(self, request):
    beads = wrapperType.objects.all()
    serializer = wrapperTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = wrapperTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

