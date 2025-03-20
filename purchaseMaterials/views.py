from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseMaterial
from .serializers import PurchaseMaterialSerializer


class PurchaseMaterialAPIView(APIView):
    """Handles creating and listing purchase materials."""

    def get(self, request):
        """List all purchased materials (Admin Only)."""
        purchases = PurchaseMaterial.objects.all()
        serializer = PurchaseMaterialSerializer(purchases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new purchase or update an existing one."""
        serializer = PurchaseMaterialSerializer(data=request.data)
        if serializer.is_valid():
            purchase = serializer.save()  # Save is now handled in the serializer
            return Response(
                {"message": "Purchase processed", "data": PurchaseMaterialSerializer(purchase).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseDeleteView(APIView):
    """Delete a purchase material."""
    def delete(self, request, pk):
        """Delete a purchase material by ID."""
        try:
            purchase = PurchaseMaterial.objects.get(pk=pk)
        except PurchaseMaterial.DoesNotExist:
            return Response({"message": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)
        purchase.delete()
        return Response({"message": "Purchase deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    