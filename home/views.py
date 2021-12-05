from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

class home(ListView):

    model = Post
    template_name = 'home.html'

class article_detail(DetailView):

    model = Post
    template_name = 'detail.html'

class article_add(CreateView):
    
    model = Post
    form_class = PostForm
    template_name = 'add.html'