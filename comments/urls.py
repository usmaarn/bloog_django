from django.urls import path
from . import views

app_name = "comment"

urlpatterns = [
    path("<int:pk>/like/", views.toggle_comment_like, name="like"),
    path("<int:pk>/liked/", views.user_liked_comment, name="liked"),
    path("new/", views.add_comment, name="create"),
    path("<int:comment_id>/replies/<int:pk>/like", views.like_reply, name="reply.like"),
    path("<int:comment_id>/replies/<int:pk>/liked", views.user_liked_reply, name="reply.liked"),
    path("<int:comment_id>/replies/new/", views.create_reply, name="reply.create"),
]
