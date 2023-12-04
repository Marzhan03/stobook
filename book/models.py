from django.db import models
from django.urls import reverse
from account import models as account_models

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
    books = models.ManyToManyField("Book", through="OrderBook")
    def __str__(self):
        return self.bookname
    def get_absolute_url(self):
        return  reverse ('post',kwargs={'post_id':self.pk})


class City(models.Model):
    city=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.city


class Street(models.Model):
    city=models.ForeignKey("City", verbose_name=("Город"), on_delete=models.CASCADE,null=True)
    street=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.street

class Address(models.Model):
    streetname=models.ForeignKey("Street",on_delete=models.PROTECT,null=True)
    housenumber=models.IntegerField()
    flatnumber=models.IntegerField()


class OrderStatuses(models.IntegerChoices):
    NEW = 0, 'Low'
    PROCESSED = 1, 'Normal'
    FINISHED = 2, 'High'


class Order(models.Model):
    to_address = models.ForeignKey("Address", on_delete=models.PROTECT)
    order_status=models.IntegerField(default=OrderStatuses.NEW, choices=OrderStatuses.choices)
    customer_user=models.ForeignKey(account_models.CustomUser,on_delete=models.PROTECT, null=True)
    is_active=models.BooleanField(default=True)


class OrderBook(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    book=models.ForeignKey("Book",on_delete=models.PROTECT)
    bookCount=models.IntegerField()





class Cardtype(models.Model):
    cardtypename=models.CharField(max_length=255)


class UserCard(models.Model):
    cardnumber=models.IntegerField()
    dateissue=models.CharField("Дата истечения", max_length=4)
    cvc=models.IntegerField()
    cardtype=models.ForeignKey("Cardtype",on_delete=models.PROTECT)

class Payment(models.Model):
    order=models.ForeignKey("Order",on_delete=models.PROTECT)
    date=models.DateTimeField(verbose_name="Дата и время оплата", auto_now_add=True)
    card=models.ForeignKey("UserCard",on_delete=models.PROTECT)
    summa=models.FloatField(verbose_name="Сумма")