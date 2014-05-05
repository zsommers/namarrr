from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """Override default AuthenticationForm with bootstrap classes"""
    attr = {'class': 'form-control'}
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput(attrs=attr))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attr))
