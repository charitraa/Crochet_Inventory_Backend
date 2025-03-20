from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import keyringType
from .serializers import keyringTypeSerializer

# Create your views here.

class KeyringView(APIView):
  def get(self, request):
    beads = keyringType.objects.all()
    serializer = keyringTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = keyringTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

