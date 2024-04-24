import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return f" User={self.user.username}, {self.content_type.name}={self.content_object.id}"

    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id"])]


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return f" User={self.user.username}, {self.content_type.name}={self.content_object.id}"

    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id"])]


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return f" User={self.user.username}, {self.content_type.name}={self.content_object.id}"

    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id"])]


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    followers = GenericRelation(Follow, related_query_name="tag")

    def __str__(self):
        return self.name
