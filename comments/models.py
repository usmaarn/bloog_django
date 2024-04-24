from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation

from posts.models import Post
from users.models import Like


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like, related_query_name='comment')
    
    class Meta:
        ordering = ["-date", "-modified"]
        

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like, related_query_name='reply')
    
    class Meta:
        ordering = ["-date", "-modified"]