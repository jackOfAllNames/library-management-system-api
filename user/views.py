from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()
# Function-based view for the home page
def HomePage(request):
    return JsonResponse({"message": "Welcome to the Book API!"})


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
