from django.test import TestCase
from .models import Category

class BookTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="test")

    def test_books_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_book_create(self):
        response = self.client.post('/books/create/', {
                'name': 'test book',
                'category': self.category.id
            })
        self.assertEqual(response.status_code, 302)