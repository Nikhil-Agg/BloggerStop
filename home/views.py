from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     context = {}
#     return render(request, 'home.html', context=context)

class home(ListView):

    model = Post
    template_name = 'home.html'

class article_detail(DetailView):

    model = Post
    template_name = 'detail.html'