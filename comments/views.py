from django.shortcuts import redirect, HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, Http404, JsonResponse
from django.core.exceptions import PermissionDenied
from django.urls import reverse


from posts.models import Post
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
from users.models import Like
from api.serializers import CommentSerializer


def comments_list(request, post_slug):
    try:
        post = get_object_or_404(Post, slug=post_slug)
        data = CommentSerializer(post.comment_set.all(), many=True).data
        return render(
            request,
            "comments/index.html",
            {"post": post, "form": ReplyForm()},
        )
    except Post.DoesNotExist:
        raise Http404()


@login_required
def add_comment(request, post_slug):
    try:
        if request.method != "POST":
            return HttpResponseNotAllowed(permitted_methods=["POST"])
        post = get_object_or_404(Post, slug=post_slug)
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    except Post.DoesNotExist:
        raise Http404()
    return redirect(reverse("posts:show", args=[post.slug]) + "#comments")


@login_required
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(instance=comment)

    if comment.user != request.user:
        return HttpResponse(status=405)

    if request.method == "POST":
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("posts:show", args=[comment.post.slug]) + f"#comments-{comment.id}")
    return render(
        request, "comments/edit.html", {"form": form}
    )


@login_required
def delete_comment(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect(reverse("posts:show", args=[comment.post.slug])+ f"#comments")


@login_required
def toggle_comment_like(request, post_slug, pk):
    comment = get_object_or_404(Comment, pk=pk)
    liked = Like.objects.filter(
        comment__id=comment.id, user__id=request.user.id
    ).first()
    if liked:
        liked.delete()
        return redirect(
            reverse("posts:show", args=[comment.post.slug]) + f"#comments-{comment.id}"
        )
    else:
        like = Like(content_object=comment, user=request.user)
        like.save()
        return redirect(
            reverse("posts:show", args=[comment.post.slug]) + f"#comments-{comment.id}"
        )


def user_liked_comment(request, post_slug, pk):
    comment = get_object_or_404(Comment, pk=pk)
    liked = Like.objects.filter(
        comment__id=comment.id, user__id=request.user.id
    ).exists()
    return JsonResponse({"liked": liked})


# REPLIES METHODS
@login_required
def create_reply(request, post_slug, comment_id):
    try:
        if request.method != "POST" or not post_slug:
            return HttpResponseNotAllowed(permitted_methods=["POST"])
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(slug=post_slug)
            comment = Comment.objects.get(pk=comment_id)
            reply = form.save(commit=False)
            reply.comment = comment
            reply.user = request.user
            reply.save()
            return redirect(
                reverse("posts:show", args=[post.slug]) + f"#c-{comment_id}-r-{reply.id}"
            )
    except Exception as e:
        raise e
    except Post.DoesNotExist or Comment.DoesNotExist:
        raise Http404()


@login_required
def edit_reply(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    form = ReplyForm(instance=reply)
    if reply.user != request.user:
        raise PermissionDenied()
    if request.method == "POST":
        form = ReplyForm(instance=reply, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("posts:show", args=[reply.comment.post.slug]) + f"#c-{reply.comment_id}-r-{pk}"
            )
    return render(request, "replies/edit.html", {"form": form})


@login_required
def delete_reply(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    reply = get_object_or_404(Reply, pk=pk)
    if reply.user != request.user:
        raise PermissionDenied()
    reply.delete()
    return redirect(
        reverse("posts:show", args=[reply.comment.post.slug]) + f"#c-{reply.comment_id}-replies"
    )


@login_required
def like_reply(request, post_slug, comment_id, pk):
    if request.method != "POST":
        return HttpResponse(status=405, content="Method not Allowed")
    post = get_object_or_404(Post, slug=post_slug)
    reply = get_object_or_404(Reply, pk=pk)
    liked = Like.objects.filter(reply__id=reply.id, user__id=request.user.id).first()
    if liked:
        liked.delete()
    else:
        like = Like(content_object=reply, user=request.user)
        like.save()
    return redirect(
        reverse("posts:show", args=[post.slug]) + f"#c-{comment_id}-r-{reply.id}"
    )


def user_liked_reply(request, post_slug, comment_id, pk):
    reply = get_object_or_404(Reply, pk=pk)
    liked = Like.objects.filter(
        reply__id=reply.id, user__id=request.user.id
    ).exists()
    return JsonResponse({"liked": liked})