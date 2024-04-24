from django.urls import path

from dashboard import views
from posts import views as post_views
from comments import views as comment_views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),

    path("posts/new", post_views.new_post, name="posts.create"),
    path("posts/<int:pk>/edit", post_views.edit_post, name="posts.update"),
    path("posts/<int:pk>/delete", post_views.delete_post, name="posts.delete"),

    path("comments/", views.comments, name='comments'),
    path("comment/new", comment_views.add_comment, name="comments.create"),
    path("comment/<int:pk>/edit", comment_views.update_comment, name="comments.update"),
    path("comment/<int:pk>/delete", comment_views.delete_comment, name="comments.delete"),

    path("replies/", views.replies, name='replies'),
    path("replies/new", comment_views.create_reply, name="replies.create"),
    path("replies/<int:pk>/edit", comment_views.edit_reply, name="replies.update"),
    path("replies/<int:pk>/delete", comment_views.delete_reply, name="replies.delete"),

    path("settings/", views.settings_view, name='settings'),
]