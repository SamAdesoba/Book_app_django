from django.urls import path

from my_app import views_functional
from . import views


app_name = 'my_app'

urlpatterns = [
    # path('', views.redirect),
    # path('index/', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('book-list/', views.book_list, name='book-list'),
    # path('book-list-fiction/', views.book_list_for_fiction, name='book-list-fiction'),
    # path('book-list-price/', views.book_list_for_price, name='book-list-price'),
    # path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),


    path('books/', views_functional.book_list, name='book-list'),
    path('books/<int:pk>/', views_functional.book_detail, name='book-detail'),


    path('publishers/', views_functional.publisher_list, name='publisher-list'),
    path('publishers/<int:pk>/', views_functional.publisher_detail, name='publisher-detail'),

]
