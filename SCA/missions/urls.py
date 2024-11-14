from .views import MissionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'missions', MissionViewSet)

urlpatterns = router.urls