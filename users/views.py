from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from .serializers import UserCreateSerializer, UserUpdateSerializer
from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

class UserDetails(APIView):
    permission_classes = [IsSuperuserOrAdmin]
    def get(self,pk, format=None):
        users = User.objects.get(pk=pk)
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk, format=None):
            user = User.objects.get(pk=pk)
            serializer = UserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, pk, format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserCreate(APIView):
    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# user view for admin
class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
            user = User.objects.get(pk=pk)
            serializer = UserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AdminUserDetails(APIView):
#      permission_classes = [LoginRequiredPermission]