from django.urls import path
#from . import views
from blog import views
from .views import *


urlpatterns = [
    #path('',views.home, name= 'homepage'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name = 'update_post' ),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name = 'delete_post' ),
    path('category/<str:category_name>', CategoryView, name="category"),
    path('num_visits/',views.sessfun, name= 'session'),

]
