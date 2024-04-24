from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404
from uuid import uuid4


from .models import Post
from . import forms
from comments.forms import CommentForm, ReplyForm
from users.models import Like, Bookmark
from posts.utils import estimate_reading_time


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        "posts": posts
    })
    

def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    try:
        form = CommentForm()
        post = Post.objects.get(slug=slug)
        liked = Like.objects.filter(user__id=request.user.id, post__id=post.id).exists()
        bookmarked = Bookmark.objects.filter(user__id=request.user.id, post__id=post.id).exists()
    except Post.DoesNotExist:
        raise Http404()
    return render(request, 'posts/show.html', {
        "post": post, "form": form, "liked": liked, "bookmarked": bookmarked,
    })


@login_required(login_url='/login/')
def new_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = uuid4()
            post.author = request.user
            post.read_time = estimate_reading_time(post.body)
            post.save()
            return redirect("posts:index")
    else: 
        form = forms.PostForm()
    return render(request, 'posts/create.html', {
        "form": form
    })
    
    
@login_required(login_url='/login/')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = forms.PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            updated_post = form.save(commit=False)
            post.read_time = estimate_reading_time(post.body)
            updated_post.save()
            return redirect("posts:show", post.slug)
    else: 
        form = forms.PostForm(instance=post)
    return render(request, 'posts/edit.html', {
        "form": form, "post": post
    })
    

@login_required(login_url='/login/')
def delete_post(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if request.method == 'POST':
        post.delete()
        return redirect("posts:index")
    else:
        return render(request, 'posts/delete.html', {"post": post})
    
    
@login_required(login_url='/login')
def like_post(request, pk):
    try:
        if request.method != 'POST':
            return HttpResponse(status=405, content="Method not Allowed")
        post = Post.objects.get(pk=pk)
        liked = Like.objects.filter(post__id=post.id, user__id=request.user.id).first()
        if liked:
            liked.delete()
        else:    
            like = Like(content_object=post, user=request.user)
            like.save()
        return redirect("posts:show", post.slug)
    except Post.DoesNotExist:
        raise Http404()


@login_required(login_url='/login')
def bookmark_post(request, pk):
    if request.method != 'POST':
        return HttpResponse(status=405, content="Method not Allowed")
    post = Post.objects.get(pk=pk)
    bookmarked = Bookmark.objects.filter(post__id=post.id, user__id=request.user.id).first()
    if bookmarked:
        bookmarked.delete()
    else:    
        bookmark = Bookmark(content_object=post, user=request.user)
        bookmark.save()
    return redirect("posts:show", post.slug)