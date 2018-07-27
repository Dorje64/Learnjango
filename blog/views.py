from django.shortcuts import render
from blog.models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {'posts': Post.objects.all()})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
