from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel/', include('hotel.urls')),
    path('v1/drf-auth/', include('rest_framework.urls')),
]

