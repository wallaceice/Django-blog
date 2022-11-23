from django import forms
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import *

# Create your views here.


# def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDeatailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['title', 'title_tag', 'author', 'body']
    title = forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'aaaaaaa'})
    title_tag = forms.TextInput(attrs={'class': 'form-control'}),
    author = forms.Select(attrs={'class': 'form-control'}),
    body = forms.Textarea(attrs={'class': 'form-control'})
