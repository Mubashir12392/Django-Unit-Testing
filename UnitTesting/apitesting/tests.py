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


class BookDetailViewTests(APITestCase):

    def setUp(self):
        # Create a sample book for testing
        self.book = Book.objects.create(title='Sample Book', author='Author Name')

    def test_get_book(self):
        """Test retrieving a book detail"""
        url = reverse('book-detail', kwargs={'pk': self.book.pk})  # Adjust 'book-detail' based on your URL configuration
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, BookSerializer(self.book).data)

    def test_put_book(self):
        """Test updating a book detail"""
        url = reverse('book-detail', kwargs={'pk': self.book.pk})  # Adjust 'book-detail' based on your URL configuration
        data = {'title': 'Updated Book Title', 'author': 'Updated Author'}
        response = self.client.put(url, data, format='json')
        
        self.book.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book.title, 'Updated Book Title')
        self.assertEqual(self.book.author, 'Updated Author')

    def test_delete_book(self):
        """Test deleting a book detail"""
        url = reverse('book-detail', kwargs={'pk': self.book.pk})  # Adjust 'book-detail' based on your URL configuration
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())  # Verify that the book is deleted