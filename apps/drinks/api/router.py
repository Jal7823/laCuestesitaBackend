from rest_framework.routers import DefaultRouter
from apps.drinks.api.views import DrinksViewSet

router = DefaultRouter()
router.register(r'', DrinksViewSet, basename='drinks')

urlpatterns = router.urls
