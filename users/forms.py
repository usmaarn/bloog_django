from django.contrib.auth.models import User
from django import forms


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100, min_length=3)
    last_name = forms.CharField(label='First Name', max_length=100, min_length=3)
    username = forms.CharField(label='Username', max_length=100, min_length=5)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']