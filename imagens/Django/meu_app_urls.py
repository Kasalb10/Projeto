from django.urls import path
from . import views

urlpatterns = [
    # Mapeia a raiz do aplicativo diretamente para a função home na views.py
    path('', views.home, name='home'),
]
