from django.urls import path
from . import views

urlpatterns = [
    # If you go to an empty location take us to views.post_list
    path('', views.post_list, name='post_list'),
]