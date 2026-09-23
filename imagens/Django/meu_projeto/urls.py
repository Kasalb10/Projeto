from django.contrib import admin
from django.urls import path, include  # Importação do include para conectar os blocos

urlpatterns = [
    path('admin/', admin.site.urls),
    # Encaminha qualquer rota vazia para o arquivo de rotas interno do aplicativo
    path('', include('meu_app.urls')), 
]
