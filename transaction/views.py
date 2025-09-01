from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import TransactionSerializer

class BookCheckoutView(ListAPIView):
    serializer_class = TransactionSerializer
