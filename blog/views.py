from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import *
# Create your views here.


#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDeatailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
