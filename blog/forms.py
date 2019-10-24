from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # second step of creating the form, Django knows how to create a title and text field
    class Meta:
        model = Post
        fields = ('title', 'text')