from .router import router
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('consumer.urls')),
    # so this is the api url and it will go like domain/api/outfit
    path('api/', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
