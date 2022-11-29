from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
# Create your views here.

# def home(request):
#    return render(request, 'home.html', {})

def CategoryView(request,category_name):
    category_posts = Post.objects.filter(category = category_name)
    return render(request, 'categories.html', {'category_name':category_name, 'category_posts' : category_posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publish_date']
    
    def get_context_data(self, *args, **kwargs):
        category_menu =  Category.objects.all()
        context =  super(HomeView,self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        category_menu =  Category.objects.all()
        context =  super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class AddPostView(CreateView):
    form_class = PostForm
    #fields = ['title', 'title_tag', 'author', 'body']
    template_name = 'add_post.html'
    model = Post

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm

    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url =  reverse_lazy('home')



class AddCategoryView(CreateView):
    #form_class = PostForm
    #fields = ['title', 'title_tag', 'author', 'body']
    template_name = 'add_category.html'
    model = Category
    fields = "__all__"
