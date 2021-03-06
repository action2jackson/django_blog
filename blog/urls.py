from django.urls import path
from . import views
# Using built in django views login functionality!
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 127.0.0.1:8000 --> Local
    # mydjangosite.com --> Online
    # If you go to an empty location take us to views.post_list
    path('', views.post_list, name='post_list'),

    # 127.0.0.1:8000/post/2 == You will be taken to the post that has a primary key of 2
    # <int == You need to put in a number
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 2.2.2.2. plug it into urls to find it in views
    # 127.0.0.1:8000/post/new = local
    path('post/new/', views.post_new, name='post_new'),

    # checks post, which post, and then sends to post_edit function in view
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('drafts/', views.post_draft_list, name='post_draft_list'),

    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('comment/<int:pk>/remove/', views.remove_comment, name='remove_comment'),

    path('comment/<int:pk>/approve', views.approve_comment, name='approve_comment'),

    path('signup/', views.signup, name='signup'),
]