from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment
# Django built in crispy_forms (get from django crispy_forms github)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(forms.ModelForm):
    # second step of creating the form, Django knows how to create a title and text field
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

# Before I created this form I needed to pip install django-crispy-forms, which adds it to the requirements.txt app
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up', 'Sign up', css_class='btn-primary'))
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)