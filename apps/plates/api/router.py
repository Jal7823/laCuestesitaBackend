from rest_framework.routers import DefaultRouter
from .views import PlatesViewSet

router = DefaultRouter()
router.register(r'', PlatesViewSet)

urlpatterns = router.urls
