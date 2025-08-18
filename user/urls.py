from django.urls import path, include
from .views import HomePage
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    # path('', include(router.urls)),
    path('', HomePage, name='home'),
]
