from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserCreateSerializer


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
        if user is not None:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            request.session['access_token'] = str(access_token)

            return Response({
                'access': str(access_token),
                'refresh': str(refresh),
                'message':'Login sucessfull',
                'data':user
            }, status=status.HTTP_200_OK)

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