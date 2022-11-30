from django.urls import path
from iris import views
from iris.views import *

urlpatterns = [
    # homepage da nossa aplicação web. Dentro de views, irá usar a classe HomeView para abrir a página .html (index.html). Essa classe será implementada a seguir
    path('', views.HomeViewIris.as_view(), name='chart'),
]
