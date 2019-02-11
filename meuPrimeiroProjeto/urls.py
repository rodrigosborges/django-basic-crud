from django.contrib import admin
from django.urls import path, include
from .views import hello, articles, fname
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as cliente_urls

urlpatterns = [
    path('clientes/', include(cliente_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
