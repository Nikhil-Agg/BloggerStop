from django.urls import path
# from . import views
from .views import home, article_detail

urlpatterns = [
    # path('', views.home, name='home'),
    path('', home.as_view(), name='home'),
    path('post/<int:pk>', article_detail.as_view(), name='detail'),
]
