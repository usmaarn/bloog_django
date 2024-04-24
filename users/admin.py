from django.contrib import admin

from .models import Tag, Like, Bookmark

admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Bookmark)