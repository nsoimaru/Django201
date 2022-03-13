from django.views.generic import ListView

from .models import Post

# Create your views here.

class HomePage(ListView):
    http_method_names = ['get']
    template_name = 'feed/homepage.html'
    model = Post
    context_object_name = 'post'
    query_set = Post.objects.all().order_by('-id')[0:300]