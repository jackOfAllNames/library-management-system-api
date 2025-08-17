from django.urls import path
from .views import BookListCreateView, HomePage, BookCreateView

urlpatterns = [
    path('', HomePage, name='home'),
    path('books/', BookListCreateView.as_view(), name='books-list-create'),
    # path('books/add', BookCreateView.as_view(), name='book-create'),
]
