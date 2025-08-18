from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics

# Function-based view for the home page
def HomePage(request):
    return JsonResponse({"message": "Welcome to the Book API!"})


class RegisterView(generics.CreateAPIView):
    from .serializers import UserSerializer
    serializer_class = UserSerializer
