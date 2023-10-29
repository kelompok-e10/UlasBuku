from django.test import TestCase

# Create your tests here.
class BookTest(TestCase):
    def test_api_books_returns_json(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response['Content-Type'], 'application/json')
