from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import  UserUpdateSerializer, UserSerializer, AdminAddUserSerializer

from permissions.permissions import LoginRequiredPermission, IsSuperuserOrAdmin

# user view for admin

class UserDetails(APIView):
    """
    Admin view for user to get details, update, and delete
    """
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]

    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)  # many=True removed, since it's a single object
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None): 
        try:
            user = User.objects.get(pk=pk)
            serializer = UserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User data updated successfully', 'data': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
class UserCreate(APIView):
    """ Admin Create a new user"""
    permission_classes = [LoginRequiredPermission, IsSuperuserOrAdmin]

    def post(self, request, format=None):
        serializer = AdminAddUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserListView(APIView):
    """ Admin view a user list """
    permission_classes = [LoginRequiredPermission,IsSuperuserOrAdmin]
    def get(self, request, format=None):
        users = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


