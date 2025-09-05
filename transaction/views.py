from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from book.models import Book
from .models import Transaction

class TransactionListView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": f"Book with id - {book_id} not found"}, status=status.HTTP_404_NOT_FOUND)

    if book.available_copies < 1:
        return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
    
    book.available_copies -= 1
    book.save()

    Transaction.objects.create(
        user_id=request.user,
        book_id=book,
        action='borrow'
    )

    return Response({"message": f"Book '{book.title}' checked out successfully"}, status=status.HTTP_200_OK)    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": f"Book with id - {book_id} not found"}, status=status.HTTP_404_NOT_FOUND)

    if book.available_copies >= book.total_copies:
        return Response({"error": "All copies are already in the library"}, status=status.HTTP_400_BAD_REQUEST)
    
    book.available_copies += 1
    book.save()

    Transaction.objects.create(
        user_id=request.user,
        book_id=book,
        action='return'
    )

    return Response({"message": f"Book '{book.title}' returned successfully"}, status=status.HTTP_200_OK)