from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
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
    form_class = PostForm
    #fields = ['title', 'title_tag', 'author', 'body']
    template_name = 'add_post.html'
    model = Post
