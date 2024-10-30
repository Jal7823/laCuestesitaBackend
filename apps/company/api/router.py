from rest_framework.routers import DefaultRouter
from apps.company.api.views import CompanyViewSet

router = DefaultRouter()
router.register(r'', CompanyViewSet, basename='company')

urlpatterns = router.urls