from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class article_update(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    login_url = '/users/login/'
    template_name = 'home/edit.html'

class article_delete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'home/delete.html'
    login_url = '/users/login/'
    success_url = reverse_lazy('home')