from django.shortcuts import render
from rest_framework.views import APIView

from comments.models import Comment
from .serializers import CommentSerializer


class CommentListView(APIView):
    def get(self, request, format=None):
        pass
