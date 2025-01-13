from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from health_check import urls as health_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    
    path('health/', include(health_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)