from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db import connection

# Create your views here.
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer, PublisherSerializer
from my_app.models import Book, Publisher


# def index(request):
#     obj = [1, 2, 3, 4]
#     name = "Adesoba"
#     text = "Developed aBlock Numerical Integration Formulae for Solving Fourth Order Initial Value Problems of " \
#            "Ordinary Differential Equations using Maple and Matlab programming languages. "
#     return render(request, 'my_app/index.html', context={'name': name, 'obj': obj, 'is_major': True, 'text': text})
#
#
# def about(request):
#     return render(request, 'my_app/about.html')
#
#
# def redirect(request):
#     return HttpResponseRedirect(reverse('my_app:index'))
#
#
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'my_app/book-list.html', {'books': list(books)})
#
#
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#         return render(request, 'my_app/book-detail.html', {'book': book})
#     except Book.DoesNotExist:
#         return HttpResponse("Book does not exist")
#     # OR
#     # book = get_object_or_404(Book, pk=pk)
#     # return render(request, 'my_app/book-detail.html', {'book': book})
#
#
# def book_list_for_fiction(request):
#     books = Book.objects.filter(genre='FICTION')
#     return render(request, 'my_app/book-list-fiction.html', {'books': list(books)})
#
#
# def book_list_for_price(request):
#     books = Book.objects.filter(price__lt=80)
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3))
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('title')
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('-title')
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('-title', 'price')
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('-title', 'price').earliest()
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('-title', 'price').reverse()
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('-title', 'price').latest()
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).order_by('-title', 'price')[0]
#     # values will return a dictionary of book
#     # only will return objects
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).only('-title', 'price')
#     # books = Book.objects.filter(publisher__id__in=(1, 7, 3)).values('-title', 'price')
#     # select related gets only related objects from the database
#     # books = Book.objects.select_related('publisher').all()
#     # books = Book.objects.prefetch_related('publisher').all()
#
#     # cursor = connection.cursor()
#     # result = cursor.execute("select * from my_app_book")
#     # result.fetchAll()
#     # cursor.close()
#
#     # to update
#     # Book.objects.filter(title='ades').update()
#
#     # to delete
#     # Book.objects.filter(title='ades').delete()
#
#     #
#     # books = Book.objects.raw("select * from my_app_book")
#     # return render(request, 'my_app/book-list-fiction.html', {'books': list(books)})
#
#     return render(request, 'my_app/book-list-price.html', {'books': list(books)})
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        query_set = Book.objects.all()
        serializer = BookSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    if request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def publisher_list(request):
    if request.method == 'GET':
        query_set = Publisher.objects.all()
        serializer = PublisherSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view()
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher, context={'request': request})
        return Response(serializer.data)
    if request.method in ("PUT", "PATCH"):
        serializer = PublisherSerializer(publisher, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
