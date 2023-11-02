
from . import  views
from .views import *
from django.urls import path


urlpatterns = [
    path('', main,name='home'),
    path('book/',book,name='book'),
    path('genre/<int:genre_id>/',genres,name='genre'),
    path('post/<int:post_id>/',posts,name='post'),
    path('order',order,name='order'),
]
