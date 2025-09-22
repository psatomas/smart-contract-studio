from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics
from .models import BlockchainEvent
from .serializers import BlockchainEventSerializer

def index(request):
    return HttpResponse("Hello, this is the core index page!")

def hello_world(request):
    return JsonResponse({"message": "Hello from Django"})

def get_contracts(request):
    contract = {"id": 1, "name": "Test Contract", "status": "active"}
    return JsonResponse({"contracts": [contract]})

def get_users(request):
    return JsonResponse({"users": []})

def get_transactions(request):
    return JsonResponse({"transactions": []})

def receive_blockchain_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tx_hash = data.get("tx_hash")
        value = data.get("value")
        print("Received from blockchain:", data)
        # You could save to your Django models here
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "POST required"}, status=400)

class BlockchainEventCreateView(generics.CreateAPIView):
    queryset = BlockchainEvent.objects.all()
    serializer_class = BlockchainEventSerializer

