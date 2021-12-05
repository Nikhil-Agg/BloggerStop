from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import *

class home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_no']

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

class article_delete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')