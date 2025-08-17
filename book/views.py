from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework import generics

def BookListSerialized(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


def HomePage(request):
    return JsonResponse({"message": "Welcome to the Book API!"})


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
