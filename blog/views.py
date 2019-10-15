from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

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