"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from iris import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('member/', include('members.urls')),
    path('game/', include('game.urls')),
    # homepage da nossa aplicação web. Dentro de views, irá usar a classe HomeView para abrir a página .html (index.html). Essa classe será implementada a seguir
    path('chart/', views.HomeViewIris.as_view()),
    # api onde serão armazenados nossos dados estruturados para criação dos gráficos. Será definido depois
    path('api/', views.ListIris.as_view()),
    #path('chart/', include('iris.urls')),


]
