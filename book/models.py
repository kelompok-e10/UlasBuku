from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    author = models.CharField(max_length=1000, null=True, blank=True)
    publisher = models.CharField(max_length=1000, null=True, blank=True)
    year = models.IntegerField()
    isbn = models.CharField(max_length=1000, null=True, blank=True)
    image_url_s = models.URLField(max_length=1000, null=True, blank=True)
    image_url_m = models.URLField(max_length=1000, null=True, blank=True)
    image_url_l = models.URLField(max_length=1000, null=True, blank=True)