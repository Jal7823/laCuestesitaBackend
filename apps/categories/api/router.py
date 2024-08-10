from rest_framework.routers import DefaultRouter
from apps.categories.api.views import CategoriesViewSet

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')

urlpatterns = router.urls
