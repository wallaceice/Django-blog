from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
# Create your views here.

# def home(request):
#    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publish_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


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
