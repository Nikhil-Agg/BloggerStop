from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import *

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

class article_update(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit.html'