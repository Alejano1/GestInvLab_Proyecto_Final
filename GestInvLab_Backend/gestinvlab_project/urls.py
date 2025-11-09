# Archivo: gestinvlab_project/urls.py

from django.contrib import admin
from django.urls import path, include
# --- IMPORTA ESTA LÍNEA ---
from rest_framework.authtoken import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta línea ya la tenías:
    path('api/inventory/', include('inventory.urls')), 
    
    # --- AÑADE ESTA LÍNEA (la que da el error) ---
    path('api-token-auth/', views.obtain_auth_token),
]