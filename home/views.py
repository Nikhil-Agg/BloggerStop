from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import *

class home(ListView):
    model = Post
    template_name = 'home/home.html'
    ordering = ['-created_no']

class article_detail(DetailView):
    model = Post
    template_name = 'home/detail.html'

class article_add(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home/add.html'

class article_update(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'home/edit.html'

class article_delete(DeleteView):
    model = Post
    template_name = 'home/delete.html'
    success_url = reverse_lazy('home')