from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    # second step of creating the form, Django knows how to create a title and text field
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)