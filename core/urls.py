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
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # AUTH
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # PRODUCTS
    path(
        "api/ingredients/", include("apps.ingredients.api.router")
    ),  # Rutas de Ingredients
    path("api/drinks/", include("apps.drinks.api.router")),  # Rutas de Drinks
    path(
        "api/categories/", include("apps.categories.api.router")
    ),  # Rutas de Categories
    path("api/plates/", include("apps.plates.api.router")),
    path("api/users/", include("apps.users.api.router")),  # Rutas de Plates
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
