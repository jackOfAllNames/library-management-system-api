from django.urls import path
from .views import BookListView, HomePage

urlpatterns = [
    path('', HomePage, name='home'),
    path('books/', BookListView.as_view(), name='books'),
]
