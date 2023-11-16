

from .views import *
from django.urls import path


urlpatterns = [
    path('', main,name='home'),
    path('book/',book,name='book'),
    path('basket/',basket,name='basket'),
    path('genre/<int:genre_id>/',genres,name='genre'),
    path('post/<int:post_id>/',posts,name='post'),
    path('order',order,name='order'),
    # path('card_types', get_card_types),
    path('cities', get_cities),
    # path('load-streets/', load_streets, name='load_streets'),
    path('streets/<int:city_id>', get_streets_by_city),
    
]

