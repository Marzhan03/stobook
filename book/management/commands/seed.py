from django.core.management.base import BaseCommand, CommandError
from book import models
import json


class Command(BaseCommand):
    def create_authors(self):
        models.Author.objects.all().delete()
        with open('C:/DjangoSites/book_store_project/stobook/book/management/commands/entities_lookups/authors.json', mode="r", encoding="utf8") as file:
            authors = json.load(file)

        for author in authors.get("authors"):
            new_author = models.Author(
                name = author.get("name"),
            )

            new_author.save()

    def create_genres(self):
        models.Genre.objects.all().delete()
        with open('C:/DjangoSites/book_store_project/stobook/book/management/commands/entities_lookups/genres.json', mode="r", encoding="utf8") as file:
            genres = json.load(file)

        for genre in genres.get("genres"):
            new_genre = models.Genre(
                genrename = genre.get("genrename"),
            )

            new_genre.save()

    def create_publishers(self):
        models.Publishing.objects.all().delete()
        with open('C:/DjangoSites/book_store_project/stobook/book/management/commands/entities_lookups/publishers.json', mode="r", encoding="utf8") as file:
            publishers = json.load(file)

        for publisher in publishers.get("publishers"):
            new_publisher = models.Publishing(
                name = publisher.get("name"),
            )

            new_publisher.save()

    def create_books(self):
        models.Book.objects.all().delete()
        with open('C:/DjangoSites/book_store_project/stobook/book/management/commands/entities_lookups/books.json', mode="r", encoding="utf8") as file:
            books = json.load(file)

        for book in books.get("books"):
            new_book = models.Book(
                bookname = book.get("bookname"),
                bookimg = book.get("bookimg"),
                author = models.Author.objects.get(pk=book.get("author")),
                genre = models.Genre.objects.get(pk=book.get("genre")),
                publishing = models.Publishing.objects.get(pk=book.get("publishing")),
                number_of_pages = book.get("number_of_pages"),
                cost = book.get("cost"),
                description = book.get("description"),
            )

            new_book.save()

    def handle(self, *args, **options):
        self.create_authors()
        self.create_genres()
        self.create_publishers()
        self.create_books()
