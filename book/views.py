from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
<<<<<<< HEAD
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
=======
from .models import Book, Genre, City, Street, Address, OrderBook, Order
import json

>>>>>>> 049dd5a9771965afa8e66fc8d103aee34b35e5be
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer, StreetSerializer, OrderSerializer, PaymentSerializer

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

<<<<<<< HEAD
=======
def order(request):
    return render(request,'book/order.html', context={
        'title': "Order",
    })


# декоратор
@api_view(['GET',])
def get_card_types(request):
    card_types = Cardtype.objects.all()

    serializer = CardTypeSerializer(card_types, many=True)

    return Response(serializer.data)

@api_view(['GET',])
def get_cities(request):
    cities = City.objects.all()

    serializer = CitySerializer(cities, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_streets_by_city(request, city_id):

    # cities = City.objects.all()
    streets = Street.objects.filter(city_id=city_id)

    serializer = StreetSerializer(streets, many=True)

    return Response(serializer.data)

def order(request):
    if request.method == 'POST':
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        housenumber = request.POST.get("housenumber")
        flatnumber = request.POST.get("flatnumber")
        streetname=request.POST.get("streetname")
        address=Address.objects.filter(streetname=Street.objects.get(pk=streetname),flatnumber=flatnumber,housenumber=housenumber)

        books = json.loads(request.POST.get('books'))

        print(books)

        if address.exists():
            address=address.first()
        else:
            address=Address(
                streetname=Street.objects.get(pk=streetname),
                flatnumber=flatnumber,
                housenumber=housenumber,
            )    
            address.save()

        if (books != None):
            order = Order(
                to_address = address,
                customer_user = request.user,
            )

            order.save()

            for book in books:
                print(book)
                order_book = OrderBook(
                    order = order,
                    book = Book.objects.get(pk = book.get('id')),
                    bookCount = book.get('quantity'),
                )

                order_book.save()
                print(order_book)

    return render(request,'book/order.html' )

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

>>>>>>> 049dd5a9771965afa8e66fc8d103aee34b35e5be
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

def order(request):
    if request.method == 'POST':
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        housenumber = request.POST.get("housenumber")
        flatnumber = request.POST.get("flatnumber")
        streetname=request.POST.get("streetname")
        address=Address.objects.filter(streetname=Street.objects.get(pk=streetname),flatnumber=flatnumber,housenumber=housenumber)
        books = json.loads(request.POST.get('books'))
        if address.exists():
            address=address.first()
        else:
            address=Address(
                streetname=Street.objects.get(pk=streetname),
                flatnumber=flatnumber,
                housenumber=housenumber,
            )    
            address.save()
        if (books != None):
            order = Order(
                to_address = address,
                customer_user = request.user,
            )
            order.save()
            for book in books:
                print(book)
                order_book = OrderBook(
                    order = order,
                    book = Book.objects.get(pk = book.get('id')),
                    bookCount = book.get('quantity'),
                )
                order_book.save()
            return redirect('payment')
    return render(request,'book/order.html')


@api_view(['POST',])
def newpayment(request):
    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Возвращаем созданный объект и статус "Создано"
    if request.method == 'POST':
        card_number = request.POST.get('cardnumber')
        date_issue = request.POST.get('dateissue')
        cvc = request.POST.get('cvc')
        card_type = request.POST.get('cardtype')

        # Создаем новую карту пользователя
        user_card = UserCard.objects.create(
            cardnumber=card_number,
            dateissue=date_issue,
            cvc=cvc,
            cardtype_id=card_type
        )
        user_card.save()
    if request.method == 'POST':
        latest_object = UserCard.objects.latest('id')
        latest_object_id = latest_object.id
        order_id = request.POST.get('order') 
        summa = request.POST.get('summa')
        card_id = latest_object_id   # Предполагается, что передается ID карты

        # Создаем новый платеж
        payment = Payment.objects.create(
            order_id=order_id,
            summa=summa,
            card_id=card_id  # Передаем ID карты вместо всего объекта
        )
        payment.save()
    

def payment(request):
    cardType=Cardtype.objects.all()
    orderBook=OrderBook.objects.all()
    order = Order.objects.latest('id')  
    orderId = order.id 
    address=Address.objects.filter(id=orderId)
   
    return render(request, 'book/payment.html',{"cardType":cardType,"orderBook":orderBook,"order": order,"orderId":orderId,"address":address})    


def create_user_card(request):
    if request.method == 'POST':
        card_number = request.POST.get('cardnumber')
        date_issue = request.POST.get('dateissue')
        cvc = request.POST.get('cvc')
        card_type = request.POST.get('cardtype')

        # Создаем новую карту пользователя
        user_card = UserCard.objects.create(
            cardnumber=card_number,
            dateissue=date_issue,
            cvc=cvc,
            cardtype_id=card_type
        )

        # Возвращаем JSON-ответ с информацией о созданной карте пользователя
        return JsonResponse({'user_card_id': user_card.id})

    return JsonResponse({'error': 'Invalid request method'})    

@api_view(['GET',])
def get_user_orders(request):
    print("fgdgd",request.user.id)
    order = Order.objects.filter(customer_user__id=request.user.id,is_active=False)
    serializer = OrderSerializer(order, many=True)

    return Response(serializer.data)

