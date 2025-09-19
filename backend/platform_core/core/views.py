from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, this is the core index page!")

def hello_world(request):
    return JsonResponse({"message": "Hello from Django"})
