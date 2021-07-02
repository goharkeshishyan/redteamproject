from django.http import HttpResponse
from django.views import generic
from .models import Post
from .forms import PostForm
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
)

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class NewPost(CreateView):
    template_name = "blog/newpost_create.html"
    model = Post
    form_class = PostForm
