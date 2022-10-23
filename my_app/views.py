# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from my_app.filter import BookFilter
from my_app.models import Book, Publisher
from my_app.serializer import BookSerializer, PublisherSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    # queryset = Publisher.objects.filter(active=True)
    serializer_class = PublisherSerializer

    # def destroy(self, *args, **kwargs):
    #     book = Book.objects.get(pk=kwargs['pk']).update(active=False)
    #     serializer_class = PublisherSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'isbn', 'description']
    ordering_fields = ['title', 'price']
    ordering = ['title']
