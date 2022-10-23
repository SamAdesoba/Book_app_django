from django.urls import path
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


    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),


    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),

]
