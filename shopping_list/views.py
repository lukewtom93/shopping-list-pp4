from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class shopping_list(generic.ListView):
    model = Post
