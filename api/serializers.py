from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment, Reply
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    model = Post
    fields = ["id", "title", "slug", "body", "created_at", "updated_at", "user"]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "body", "created_at", "user"]
