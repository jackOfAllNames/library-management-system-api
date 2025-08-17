from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse

def BookListSerialized(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


def HomePage(request):
    return JsonResponse({"message": "Welcome to the Book API!"})