from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
# Create your views here.

def post_list(request):
    posts = Post.objects.published
    return render(request, 'blog/home.html', {'posts': posts})

def post_details(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED,  # Only published posts should be visible.
    )
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'blog/post_details.html', {'post': post})