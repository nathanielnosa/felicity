
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('property/', include('properties.urls')),
    path('agent/', include('agents.urls')),
]
