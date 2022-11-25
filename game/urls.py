from django.urls import path
from .views import *
#from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', game, name='game'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
