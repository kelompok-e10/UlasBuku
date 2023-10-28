from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_book(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    # return HttpResponse("Hello, world. You're at the polls index.")

