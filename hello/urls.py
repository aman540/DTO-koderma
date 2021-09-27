
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "DTO KODERMA"
admin.site.site_title = "DTO PORTAL"
admin.site.index_title = "Welcome to DTO KODERMA portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dto.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

