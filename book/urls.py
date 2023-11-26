

from .views import *
from django.urls import path


urlpatterns = [
    path('', main,name='home'),
    path('book/',book,name='book'),
    path('basket/',basket,name='basket'),
    path('genre/<int:genre_id>/',genres,name='genre'),
    path('post/<int:post_id>/',posts,name='post'),
    path('order',order,name='order'),
    path('cities', get_cities),
    path('streets/<int:city_id>', get_streets_by_city),
    path('payment/',payment,name='payment'),
    path('get_user_orders', get_user_orders),
    
]

