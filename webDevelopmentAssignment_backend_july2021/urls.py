from .router import router
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('consumer.urls')),
    # so this is the api url and it will go like domain/api/outfit
    path('api/', include(router.urls)),
]
