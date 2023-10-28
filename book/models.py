from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(null=True, blank=True, max_length=13)
    book_title = models.CharField(null=True, blank=True, max_length=255)
    book_author = models.CharField(null=True, blank=True,  max_length=255)
    year_of_publication = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(null=True, blank=True, max_length=255)
    image_url_s = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "book_book"  # Ensure the correct table name
    