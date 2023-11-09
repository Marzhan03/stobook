from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book,Genre

# Create your views here.
def main(request):
    books = Book.objects.filter(genre_id = 16)
    content={
        'title': "Main",
        'books': books,

    }
    return render(request,'book/main.html',content,)

def book(request):
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
    return render(request,'book/order.html',{'title':"Order",} )
