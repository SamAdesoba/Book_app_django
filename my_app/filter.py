from django_filters import FilterSet

from my_app.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'isbn': ['exact'],
            'title': ['exact', 'contains'],
            'date_published': ['isnull', 'year__gt'],
            'price': ['gt', 'lt']
        }
