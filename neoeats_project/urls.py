'''
URL configuration for the neoeats_project project.

Routes:
- Home
- Menu
- About
- Booking
'''

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('menu/', include('menu.urls')),
    path('about/', include('about.urls')),
    path('booking/', include('booking.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
