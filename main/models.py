from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn = models.CharField(max_length=100)
    image_urls = models.URLField(max_length=1000)