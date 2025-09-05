from django.urls import path, include
from .views import HomePage, RegisterView, ListUsersView, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    # path('users/login/', obtain_auth_token, name='login'),
    path('users/login/', TokenObtainPairView.as_view(), name='login'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('', include(router.urls)),
    # path('', ListUsersView.as_view(), name='list_users'),
]
