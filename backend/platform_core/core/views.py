from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlockchainEvent
from .serializers import BlockchainEventSerializer

class BlockchainEventReceiveView(APIView):
    """
    Receives blockchain events via POST.
    Secured with an API token in headers.
    """
    def post(self, request):
        # Step 1: Validate API token
        token = request.headers.get("X-BLOCKCHAIN-TOKEN")
        if token != getattr(settings, "BLOCKCHAIN_API_TOKEN", ""):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        # Step 2: Validate data and save
        serializer = BlockchainEventSerializer(data=request.data)
        if serializer.is_valid():
            # Step 3: Check idempotency (avoid duplicates)
            if BlockchainEvent.objects.filter(tx_hash=serializer.validated_data['tx_hash']).exists():
                return Response({"status": "already exists"}, status=status.HTTP_200_OK)

            serializer.save()
            return Response({"status": "ok"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



