from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]