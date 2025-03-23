from rest_framework.views import APIView
from rest_framework.response import Response

from permissions.permissions import IsSuperuserOrAdmin, LoginRequiredPermission

from .models import yarnType
from .serializers import yarnTypeSerializer

# Create your views here.

class yarnTypeView(APIView):
  permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]

  def get(self, request):
    beads = yarnType.objects.all()
    serializer = yarnTypeSerializer(beads, many=True)
    return Response(serializer.data)
  def post(self, request):
    serializer = yarnTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

