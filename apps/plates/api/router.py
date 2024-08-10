from rest_framework.routers import DefaultRouter
from apps.plates.api.views import PlatesViewSet

router = DefaultRouter()
router.register(r'plates', PlatesViewSet, basename='plates')

urlpatterns = router.urls
