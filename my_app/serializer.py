
from rest_framework import serializers

from my_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):  # noqa
    # book_title = serializers.CharField(max_length=255, source='title')
    # publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # # Implementing HateOases in django
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Book.objects.all(),
    #     view_name='my_app:publisher-detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'description', 'date_published', 'isbn', 'price', 'publisher']
        # fields or you can use exclude to remove few fields
#       exclude fields = ['title', 'isbn']
