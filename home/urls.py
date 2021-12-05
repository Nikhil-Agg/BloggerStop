from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('', home.as_view(), name='home'),
    path('post/<int:pk>', article_detail.as_view(), name='detail'),
    path('add/', article_add.as_view(), name='add'),
]
