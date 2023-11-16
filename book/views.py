from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book,Genre,City,Street

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer, StreetSerializer

# Create your views here.
def main(request):
    
    books = Book.objects.filter(genre_id = 16)
    content={
        'title': "Main",
        'books': books,

    }
    return render(request,'book/main.html',content,)

def book(request):
    search_query=request.GET.get('search','')
    if search_query:
        books = Book.objects.filter(bookname__icontains=search_query)
    else:
        books = Book.objects.all()
    genres=Genre.objects.all()
    context={
        'title': "Books",
        'genres': genres,
        'books': books,
        'genre_selected':0,
    }
    return render(request,'book/book.html',context=context )

def genres(request,genre_id):
    books = Book.objects.filter(genre=genre_id)
    genres = Genre.objects.all()
    context = {
        'title': "Books",
        'genres': genres,
        'books': books,
        'genre_selected': genre_id,
    }
    return render(request, 'book/book.html', context)

def posts(request,post_id):
    post=get_object_or_404(Book,pk=post_id)
    context = {
        'title': "Posty",
        'post': post,
    }
    return render(request, 'book/post.html', context)

def basket(request):
    return render(request, 'book/cart.html')



def order(request):
    cities = City.objects.all()
    return render(request,'book/order.html',{'cities':cities,} )

# def load_streets(request):
#     city_id = request.GET.get('city_id')
#     streets = Street.objects.filter(city_id=city_id)
#     streets_data = [{'id': street.id, 'name': street.street} for street in streets]
#     return JsonResponse({'streets': streets_data})    

# декоратор
# @api_view(['GET',])
# def get_card_types(request):
#     card_types = Cardtype.objects.all()
#     serializer = CardTypeSerializer(card_types, many=True)
#     return Response(serializer.data)

@api_view(['GET',])
def get_cities(request):
    cities = City.objects.all()

    serializer = CitySerializer(cities, many=True)

    return Response(serializer.data)

@api_view(['GET',])
def get_streets_by_city(request, city_id):

    # cities = City.objects.all()
    streets = Street.objects.filter(city_id=city_id)

    serializer = StreetSerializer(streets, many=True)

    return Response(serializer.data)




