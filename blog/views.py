from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {'posts': Post.objects.all()})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})