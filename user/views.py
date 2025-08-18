from django.shortcuts import render
from django.http import JsonResponse

# Function-based view for the home page
def HomePage(request):
    return JsonResponse({"message": "Welcome to the Book API!"})