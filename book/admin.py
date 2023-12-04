from django.contrib import admin

# Register your models here.
from .models import *
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_display_links = ("id","name")
    search_fields = ("name",)

admin.site.register(Author,AuthorAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ("id","genrename")
    list_display_links = ("id","genrename")
    search_fields = ("genrename",)

admin.site.register(Genre,GenreAdmin)
admin.site.register(Publishing)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","bookname")
    list_display_links = ("id","bookname")
    search_fields = ("bookname",)
admin.site.register(Book,BookAdmin)

admin.site.register(City)
admin.site.register(Street)
admin.site.register(Address)

admin.site.register(Order)
admin.site.register(OrderBook)

admin.site.register(Cardtype)
admin.site.register(Payment)
admin.site.register(UserCard)
