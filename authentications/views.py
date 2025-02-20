from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from permissions.permissions import LoginRequiredPermission
from users.serializers import UserCreateSerializer, UserSerializer, UserUpdateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication



class LoginView(TokenObtainPairView):
    """
    Custom view for user login to get access and refresh tokens.
    """
    def post(self, request, *args, **kwargs):
        # You can add additional logic here if needed for custom login
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate the user
        user = authenticate(email=email, password=password)
        user_serializer = UserSerializer(user)
        if user is not None:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            response  = Response({
                'message':'Login sucessfull',
                'data':user_serializer.data,
                'access': str(access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)

            response.set_cookie(
            key="access_token",
            value=str(access_token),
            httponly=True,  # Prevent JavaScript access (security)
            secure=True,  # Use HTTPS
            samesite="Lax", 
            )
            return response

        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class CreateUserView(APIView):
    """
    Custom view for user registration.
    """
    def post(self, request, *args, **kwargs):
        # You can add additional logic here if needed for custom registration
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

class GetUserDataView(APIView):

    """
    View to get the logged-in user's own data from the session.
    """
    permission_classes = [LoginRequiredPermission]

    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get('access_token')

        auth = JWTAuthentication()
        validated_token = auth.get_validated_token(token)
        user = auth.get_user(validated_token)

        if not user:
            return Response({"message": "Invalid token"}, status=401)

        try:
            userData = UserSerializer(user)
            return Response({
                'data': userData.data,
                "message": "User data retrieved successfully"
            }, status=200)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=404)
        

class UpdateUserView(APIView):
    permission_classes = [LoginRequiredPermission]

    def put(self, request, *args, **kwargs):
        token = request.COOKIES.get('access_token')

        if not token:
            return Response({"message": "Access token missing"}, status=status.HTTP_401_UNAUTHORIZED)

        auth = JWTAuthentication()
        try:
            validated_token = auth.get_validated_token(token)
            user = auth.get_user(validated_token)
        except Exception as e:
            return Response({"message": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)  # Allow partial updates

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [LoginRequiredPermission]

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist the refresh token
            except Exception:
                return Response({"message": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)

        # Remove tokens from cookies
        response = Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response
