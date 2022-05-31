from django.test import TestCase
from .models import Book

# Testing the model
class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testbook = Book.objects.create(title = "test_book", description="Testing book")
        testbook.save()


    def test_books_model(self):
        book = Book.objects.get(id=1)
        actual_title = book.title
        actual_description = book.description
        self.assertEqual(actual_title, "test_book")
        self.assertEqual(actual_description, "Testing book")

    
