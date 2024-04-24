from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django_ckeditor_5.fields import CKEditor5Field

from users.models import Like, Bookmark, Tag


class Post(models.Model):
    title = models.CharField(max_length=75, unique=True, null=False)
    body = CKEditor5Field(null=False)
    slug = models.CharField(max_length=255, unique=True, null=False)
    banner = models.ImageField(default='fallback.png', blank=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    read_time = models.CharField(max_length=50, null=False, default="5")
    views = models.IntegerField(default=0)
    likes = GenericRelation(Like, related_query_name="post")
    bookmarks = GenericRelation(Bookmark, related_query_name="post")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-date"]


