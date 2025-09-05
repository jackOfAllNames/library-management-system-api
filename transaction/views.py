from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from book.models import Book

class BookCheckoutView(ListAPIView):
    serializer_class = TransactionSerializer


@api_view(['GET'])
def checkout_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": f"Book with id - {book_id} not found"}, status=status.HTTP_404_NOT_FOUND)

    if book.available_copies < 1:
        return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
    
