from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from permissions.permissions import LoginRequiredPermission
from users.serializers import UserCreateSerializer, UserSerializer
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
        # ✅ Correct way to get authenticated user ID
        token = request.COOKIES.get('access_token')  # Django stores user ID here

         # Manually authenticate user using JWT
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