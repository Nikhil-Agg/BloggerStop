from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('', home.as_view(), name='home'),
    path('post/<int:pk>', article_detail.as_view(), name='detail'),
    path('add/', article_add.as_view(), name='add'),
    path('update/<int:pk>', article_update.as_view(), name='update'),
    path('delete/<int:pk>', article_delete.as_view(), name='delete')
]
