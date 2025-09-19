from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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
