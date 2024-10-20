from django.urls import path
from . import views
from frota.views import LoginView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),  # Rota para login
]
