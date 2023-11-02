from .views import *
from django.urls import path, include

urlpatterns = [
    path('', include('book.urls')),
    path('account/', include('account.urls'))
]
