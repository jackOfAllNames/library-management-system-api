from django.urls import path
from .views import checkout_book, return_book, TransactionListView

urlpatterns = [
    path('checkout/<int:book_id>/', checkout_book, name='checkout_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),
    path('transactions/', TransactionListView.as_view(), name='list_transactions'),
]
