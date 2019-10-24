from django.urls import path
from . import views

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
]