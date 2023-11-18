from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    #htpp://127.0.0.1:8000/
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
