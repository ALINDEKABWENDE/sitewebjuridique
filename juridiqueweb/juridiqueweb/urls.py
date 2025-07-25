from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cabinet.urls')),
    path('clients/', include('clients.urls')),
    path('rdv/', include('rdv.urls')),
    path('prison/', include('prison.urls')),
    path('documents/', include('documents.urls')),
    path('statistiques/', include('statistiques.urls')),
]

