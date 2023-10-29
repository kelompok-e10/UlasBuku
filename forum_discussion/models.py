from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.

class Header(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    book_title = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()

    def get_book_info(self):
        try:
            book_info = Book.objects.get(book_title=self.book_title)
            book_info = {
                'isbn': book_info.isbn,
                'book_title': book_info.book_title,
                'author': book_info.book_author,
                'published_year': book_info.year_of_publication,
                'publisher': book_info.publisher,
                'image_url_s': book_info.image_url_s,
            }
            return book_info
        except Book.DoesNotExist:
            return None
    
class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reply = models.TextField()