from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
class RouterDetailsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        base_url = "welcome to my app"
        return Response(base_url)
