from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
class RouterDetailsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        base_url = "http://127.0.0.1:8000/"
        router_details = {
            "Welcome to the Crochet Inventory System API": f"{base_url}",
            "admin": f"{base_url}admin",
            "user": f"{base_url}user",
        }

        return Response(router_details)
