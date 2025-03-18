import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from crochet_inventory_system import settings
from .models import Order
from .serializers import OrderSerializer

class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """Fetch all orders"""
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Create a new order and assign it to the logged-in user"""

        # Get access token from session cookies
        access_token = request.COOKIES.get('access_token')

        if not access_token:
            return Response({'error': 'Access token missing'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Decode JWT to get user ID
            decoded_token = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token.get('user_id')

            if not user_id:
                return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

            # Assign user to the order
            data = request.data.copy()
            data['user'] = user_id  # Set user from token

            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user_id=user_id)  # Save order with user ID
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
