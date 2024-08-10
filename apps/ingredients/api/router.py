from rest_framework.routers import DefaultRouter
from apps.ingredients.api.views import IngredientsViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')

urlpatterns = router.urls
