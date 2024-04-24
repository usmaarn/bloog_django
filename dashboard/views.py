from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserUpdateForm


@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def posts(request):
    user_posts = request.user.post_set.all()
    return render(request, 'dashboard/posts.html', {
        'posts': user_posts
    })

@login_required
def comments(request):
    user_comments = request.user.comment_set.all()
    return render(request, 'dashboard/comments.html', {
        'comments': user_comments
    })


@login_required
def replies(request):
    user_replies = request.user.reply_set.all()
    return render(request, 'dashboard/replies.html', {
        'replies': user_replies
    })


@login_required
def settings_view(request):
    form = UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('dashboard:settings')
    return render(request, 'dashboard/settings.html', {'form': form})