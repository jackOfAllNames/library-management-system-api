from django.urls import path
from .views import BookListSerialized, HomePage

urlpatterns = [
    path('', HomePage, name='home'),
]
