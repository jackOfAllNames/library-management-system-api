from django.db import models
from book.models import Book
from user.models import CustomUser as User


class Transaction(models.Model):
    choices = (
        ('borrow', 'Borrow'),
        ('return', 'Return')
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='transactions')
    timestamp = models.DateTimeField(auto_now_add=True)
    initiated = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=10, choices=choices)
