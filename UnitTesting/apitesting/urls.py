from django.urls import path

from .views import *


urlpatterns = [
    path('api/book_list_create/', BookListView.as_view(), name='book-list'),
    path('api/book_get_update_delete/',BookDetailView.as_view(), name='book-detail')
]


