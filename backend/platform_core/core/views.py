from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlockchainEvent
from .serializers import BlockchainEventSerializer

# Health check endpoint
class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"})


# Receive blockchain data from FastAPI
class BlockchainEventReceiveView(APIView):
    def post(self, request):
        serializer = BlockchainEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "ok"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all contracts (example static response for now)
class ContractListView(APIView):
    def get(self, request):
        contract = {"id": 1, "name": "Test Contract", "status": "active"}
        return Response({"contracts": [contract]})


# Get transactions (example, empty list)
class TransactionListView(APIView):
    def get(self, request):
        return Response({"transactions": []})


