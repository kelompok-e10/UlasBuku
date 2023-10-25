from django.shortcuts import render
from book.models import Books
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def get_books(requests):
    data = Books.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

