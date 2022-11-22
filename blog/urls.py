from django.urls import path
#from . import views
from.views import *


urlpatterns = [
    #path('',views.home, name= 'homepage'),
    path('',HomeView.as_view(),name = 'home'),
    path('article/<int:pk>',ArticleDeatailView.as_view(),name = 'article-detail')

]

