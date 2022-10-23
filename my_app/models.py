from enum import unique

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.migrations import state
from django.template.defaultfilters import default


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = (
        ('COMEDY', 'Comedy'),
        ('TRAGEDY', 'Tragedy'),
        ('FICTION', 'Fiction'),
        ('NON_FICTION', 'Non Fiction'),
        ('ROMANCE', 'Romance'),
    )
    title = models.CharField(max_length=255, verbose_name="Book title")
    description = models.TextField(default="Any text", help_text="Book description")
    date_published = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=20, verbose_name="ISBN")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books", default=1)

    def __str__(self):
        return  f"{self.title} - {self.isbn}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    books = models.ManyToManyField(Book, related_name='author', through='BookAuthor')


class BookAuthor(models.Model):
    ROLES = (
        ('AUTHOR', 'Author'),
        ('CO_AUTHOR', 'C0-Author'),
        ('EDITOR', 'Editor')
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=ROLES)


class Address(models.Model):
    numbers = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default='Lagos')
    country = models.CharField(max_length=255, default='Nigeria')
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True)
