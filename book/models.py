from django.db import models
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    name=models.TextField(max_length=255)

    def __str__(self):
        return (self.name)

class Genre(models.Model):
    genrename=models.CharField(max_length=255)
    def __str__(self):
        return self.genrename
    def get_absolute_url(self):
        return  reverse ('genre',kwargs={'genre_id':self.pk})

class Publishing(models.Model):
    name=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name


class Book(models.Model):
    bookname=models.CharField(max_length=255)
    bookimg=models.ImageField(upload_to="photos/%Y/%m/%d")
    author=models.ForeignKey("Author",on_delete=models.PROTECT,null=True)
    genre=models.ForeignKey("Genre",on_delete=models.PROTECT,null=True)
    publishing=models.ForeignKey("Publishing",on_delete=models.PROTECT,null=True)
    number_of_pages=models.IntegerField()
    cost=models.IntegerField(null=True)
    description=models.TextField()
    def __str__(self):
        return self.bookname
    def get_absolute_url(self):
        return  reverse ('post',kwargs={'post_id':self.pk})


class City(models.Model):
    city=models.CharField(max_length=255)
    def __str__(self):
        return self.city


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', null=True)
    street=models.CharField(max_length=255)
    def __str__(self):
        return self.street

class Address(models.Model):
    streetname=models.ForeignKey("Street",on_delete=models.PROTECT)
    housenumber=models.IntegerField()
    flatnumber=models.IntegerField()


class Orderstatus(models.Model):
    orderstatus=models.CharField(max_length=255)

    def __str__(self):
        return self.orderstatus

class Deliveryuser(models.Model):
    deliveryfirstname=models.CharField(max_length=255)
    deliverysurname=models.CharField(max_length=255,null=True)
    telephonenumber=models.IntegerField()
    def __str__(self):
        return self.deliveryfirstname+self.deliverysurname

class CustomerUser(models.Model):
    customfirstname = models.CharField(max_length=255)
    customsurname = models.CharField(max_length=255)
    email = models.EmailField(max_length=70)
    telephonenumber = models.IntegerField()


class Order(models.Model):
    toaddress = models.ForeignKey("Address", on_delete=models.PROTECT)
    departuredate=models.DateTimeField()
    arrivaldate=models.DateTimeField()
    orderstatus=models.ForeignKey("Orderstatus",on_delete=models.PROTECT)
    deliveryuser=models.ForeignKey("Deliveryuser",on_delete=models.PROTECT)
    customeruser=models.ForeignKey("Customeruser",on_delete=models.PROTECT)


class OrderBook(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    book=models.ForeignKey("Book",on_delete=models.PROTECT)
    bookCount=models.IntegerField()

class Paymentstatus(models.Model):
    paystatus=models.CharField(max_length=255)

class Cardholder(models.Model):
    cardholdername=models.CharField(max_length=255)

class Cardtype(models.Model):
    cardtypename=models.CharField(max_length=255)


class UserCard(models.Model):
    cardholder=models.ForeignKey("Cardholder",on_delete=models.PROTECT)
    cardnumber=models.IntegerField()
    dateissue=models.DateTimeField()
    cardyear=models.IntegerField()
    cvc=models.IntegerField()
    cardtype=models.ForeignKey("Cardtype",on_delete=models.PROTECT)

class Card(models.Model):
    order=models.ForeignKey("Order",on_delete=models.PROTECT)
    paymentstatus=models.ForeignKey("Paymentstatus",on_delete=models.PROTECT)
    card=models.ForeignKey("UserCard",on_delete=models.PROTECT)