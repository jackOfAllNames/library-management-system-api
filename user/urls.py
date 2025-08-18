from django.urls import path, include
from .views import HomePage, RegisterView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    # path('', include(router.urls)),
    path('', RegisterView.as_view(), name='register'),
]
