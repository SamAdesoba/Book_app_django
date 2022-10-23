from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views


app_name = 'my_app'

router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('publishers', views.PublisherViewSet)


urlpatterns = [
    path('', include(router.urls)),
]