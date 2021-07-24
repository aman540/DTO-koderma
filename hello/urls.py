
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "DTO KODERMA"
admin.site.site_title = "DTO PORTAL"
admin.site.index_title = "Welcome to DTO KODERMA portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dto.urls'))
]
