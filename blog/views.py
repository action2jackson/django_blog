from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # lte == "less then or equal to", ONLY published blog posts get filtered
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    # Requesting access to the html file post_list
    return render(request, 'blog/post_list.html', stuff_for_frontend)