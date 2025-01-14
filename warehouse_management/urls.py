from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from health_check import urls as health_urls

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Main App (inventory)
    path('', include('inventory.urls')),

    # Health Check URLs
    path('health/', include(health_urls)),
]

# Static & Media Files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
