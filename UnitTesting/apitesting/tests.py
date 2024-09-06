from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *
from .serializers import *

# Create your tests here.

class BookListViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('book-list')
        self.book_data = {
            'name':'The Power',
            'author_name':'Maxluthor'
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_books(self):
        response = self.client.get(self.url)
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_create_book(self):
        self.data = {
            'name':'Ben 10',
            'author_name':'Jackpaul'
        }
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'],self.data['name'])
        self.assertEqual(response.data['author_name', self.data['author_name']])