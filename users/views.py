from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import  UserUpdateSerializer, UserSerializer, AdminAddUserSerializer
import os
from django.conf import settings
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


class UpdateProfileIcon(APIView):
    """ user profile picture """
    
    def post(self, request, format=None):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({"message": "Access token missing"}, status=status.HTTP_401_UNAUTHORIZED)

        auth = JWTAuthentication()
        try:
            validated_token = auth.get_validated_token(token)
            user = auth.get_user(validated_token)  # Get user directly from the token
        except Exception:
            return Response({"message": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

        # Ensure the request contains a file
        if 'profile_pic' not in request.FILES:
            return Response({"message": "No profile image provided"}, status=status.HTTP_400_BAD_REQUEST)

        profile_pic = request.FILES['profile_pic']

        # Get the existing profile icon path before updating
        old_profile_pic = user.profile_pic.path if user.profile_pic else None

        # Update the user's profile picture
        user.profile_pic = profile_pic
        user.save()

        # Delete the old profile image if it exists
        if old_profile_pic and os.path.exists(old_profile_pic):
            os.remove(old_profile_pic)

        return Response({'message': 'Profile icon updated successfully', 'data': UserSerializer(user).data})
    
class UserUpdateProfile(APIView):
    """ user update profile """
    def put(self, request, format=None):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({"message": "Access token missing"}, status=status.HTTP_401_UNAUTHORIZED)
        auth = JWTAuthentication()
        try:
            validated_token = auth.get_validated_token(token)
            user = auth.get_user(validated_token)  # Get user directly from the token
        except Exception:
            return Response({"message": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User data updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    