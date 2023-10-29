from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'book_title', 'book_author', 'year_of_publication', 'publisher', 'image_url_s']