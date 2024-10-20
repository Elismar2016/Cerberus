# cerberus_backend/urls.py
from django.urls import path, include
from frota.views import home

urlpatterns = [
    path('', home, name='home'),  # Adicione isso
    path('api/', include('frota.urls')),
]
