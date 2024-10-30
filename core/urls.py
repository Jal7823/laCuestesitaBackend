from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from apps.users.api.views import CustomTokenObtainPairView  # Asegúrate de importar tu vista personalizada

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    #COMPANY
    path("api/company/", include("apps.company.api.router")),
    # AUTH
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),  # Usa tu vista personalizada
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # PRODUCTS
    path("api/ingredients/", include("apps.ingredients.api.router")),
    path("api/drinks/", include("apps.drinks.api.router")),
    path("api/categories/", include("apps.categories.api.router")),
    path("api/plates/", include("apps.plates.api.router")),
    path("api/users/", include("apps.users.api.router")),  # Rutas de Usuarios
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
