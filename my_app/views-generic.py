from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
from my_app.models import Book, Publisher
from my_app.serializer import BookSerializer, PublisherSerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublisherListView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return BookSerializer
    #     else:
    #         return BookCreateSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request}


class PublisherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
