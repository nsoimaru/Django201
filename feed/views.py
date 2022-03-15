from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class HomePage(ListView):
    http_method_names = ['get']
    template_name = 'feed/homepage.html'
    model = Post
    context_object_name = 'posts'
    query_set = Post.objects.all().order_by('-id')[0:300]

class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'feed/detail.html'
    model = Post
    context_object_name = 'post'
