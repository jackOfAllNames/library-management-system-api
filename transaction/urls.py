from django.urls import path, include
from .views import checkout_book, return_book
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('checkout/<int:book_id>/', checkout_book, name='checkout_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),
    # path('', include(router.urls)),
    # path('', ListUsersView.as_view(), name='list_users'),
    # path('register/', RegisterView.as_view(), name='register'),
]
