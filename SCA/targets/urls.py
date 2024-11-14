from .views import TargetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'targets', TargetViewSet)

urlpatterns = router.urls