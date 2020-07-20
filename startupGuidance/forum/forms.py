from django import forms

from .models import Post

class PostForm(forms.Form):
    message = forms.CharField(label='Your Name', max_length=100)
