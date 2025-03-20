from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import beadsSize
from .serializers import breadSizeSerializer

# Create your views here.

class BeadsView(APIView):
  def get(self, request):
    beads = beadsSize.objects.all()
    serializer = breadSizeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = breadSizeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class BreadDeleteView(APIView):
  def delete(self, request, pk):
    bread = beadsSize.objects.get(pk=pk)
    bread.delete()
    return Response(status=204)