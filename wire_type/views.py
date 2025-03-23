from rest_framework.views import APIView
from rest_framework.response import Response

from permissions.permissions import IsSuperuserOrAdmin, LoginRequiredPermission

from .models import wireType
from .serializers import wireTypeSerializer

# Create your views here.

class wireTypeView(APIView):
  permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]

  def get(self, request):
    beads = wireType.objects.all()
    serializer = wireTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = wireTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

