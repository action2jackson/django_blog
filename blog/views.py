# Need this for users to sign in
from django.contrib.auth import login
# Users are basically ion read mode when not logged in
from django.contrib.auth.decorators import login_required
# Needs this to access the model = User
from django.contrib.auth.models import User
# Need these for almost every django application
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Calling the three models that we created
from blog.forms import PostForm, CommentForm, UserForm
from .models import Post, Comment

# Create your views here.
def post_list(request):
    # lte == "less then or equal to", ONLY published blog posts get filtered
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    # Requesting access to the html file post_list
    return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
    # pk == primary key
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)

# 1.1.1.1. define it in views to render the html
@login_required
def post_new(request):
    # GET request doesnt allow you to submit forms! /// POST == EX: changing something (text)
    if request.method == 'POST':
        # requesting form from forms.py (title and text)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # The user is automatically the author
            post.author = request.user
            post.save()
            # using redirect instead of render so when you refresh page it doesnt submit the form again
            return redirect('post_detail', pk=post.pk)
    else:
        # the else is basically saying run this code if its a GET request
        # form is calling the post_edit.html form, which equals the PostForm function
        form = PostForm()
        # a new stuff_for_frontend except with the form
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

# pk is so whatever blog is clicked on for edit can be found
# post_edit is very similiar to post_edit except the form is being edited instead of created
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # instead of creating a new form its just updating an already existing one
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # once save is hit on updates it redirects user to detail html page
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

# very similiar to post_list but created_date instead of published_date
@login_required
def post_draft_list(request):
    # checks that theres no published date and then orders them by created date
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)

@login_required
def post_publish(request, pk):
    # gets the post and primary key
    post = get_object_or_404(Post, pk=pk)
    # Method we created in our models.py and this were we use it
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/', pk=post.pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # set the post to the post we have gotten at the start of the function
            comment.post = post
            comment.save()
            # once save is hit on updates it redirects user to detail.html page
            return redirect('post_detail', pk=post.pk)
    else:
        # if the user doesnt want to submit something then show them the comments html page
        # because there is no comment being submitted the CommentForm() == all the comments for
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm
    return render(request, 'blog/signup.html', {'form': form})