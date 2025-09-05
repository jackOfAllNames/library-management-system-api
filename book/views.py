from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.is_superuser or request.user.role == "admin")


# Function-based view for the home page
def HomePage(request):
    return JsonResponse({"message": "Welcome to the Book API!"})


# Using ViewSets and Routers
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'isbn']
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]