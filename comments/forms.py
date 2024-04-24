from django import forms
from .models import Comment, Reply


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        fields = ['body']


class ReplyForm(forms.ModelForm):
    body = forms.CharField(label="", max_length=255)
    
    class Meta:
        model = Reply
        fields = ['body']