from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from i18n.admin import admin_i18n
from photos.admin import admin_photos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-i18n/', admin_i18n.urls),
    path('admin-photos/', admin_photos.urls),
    path('', include('frontend.urls')),
    path('api/', include('api.urls')),
    *static(settings.STATIC_URL, document_root = settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT),
    *static(settings.PUBLIC_URL, document_root = settings.PUBLIC_ROOT)
]
