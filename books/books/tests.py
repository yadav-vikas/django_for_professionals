from django.test import TestCase
from django.urls import reverse
from .models import Book,Review
from django.contrib.auth import get_user_model

class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser('reviewuser', 'reviewuser@gmail.om', 'testpass123')
        self.book = Book.objects.create(title='Harry Potter', author='JK Rowling', price='25.00')
        self.review = Review.objects.create(book=self.book, author=self.user, review='a good review')

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_view(self):
        response = self.client.get(self.book.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_detail.html')
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'a good review')
        self.assertTemplateUsed(response, 'books/book_detail.html')

