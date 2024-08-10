from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/ingredients', include('apps.ingredients.api.router')),  # Rutas de Ingredients
    path('api/drinks', include('apps.drinks.api.router')),       # Rutas de Drinks
    path('api/categories', include('apps.categories.api.router')),   # Rutas de Categories
    path('api/plates', include('apps.plates.api.router')),    
    path('api/users', include('apps.users.api.router')),   # Rutas de Plates
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

