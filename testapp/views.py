from django.shortcuts import render, get_object_or_404

from posts.models import Post
from users.models import Tag


def homepage(request):
    top_stories = Post.objects.all()[:6]
    blogs = Post.objects.all()[:6]
    tags = Tag.objects.all()
    return render(request, 'home.html', {
        'top_stories': top_stories,
        'blogs': blogs,
        'tags': tags[:6]
    })


def about(request):
    return render(request, 'about.html')


def tags_index(request):
    tags = Tag.objects.all()
    return render(request, 'tags/index.html', {
        'tags': tags
    })


def show_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'tags/show.html', {
        'tag': tag
    })