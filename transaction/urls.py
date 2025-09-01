from django.urls import path, include
# from .views import RegisterView, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # path('users/login/', obtain_auth_token, name='login'),
    # path('', include(router.urls)),
    # path('', ListUsersView.as_view(), name='list_users'),
    # path('register/', RegisterView.as_view(), name='register'),
]
