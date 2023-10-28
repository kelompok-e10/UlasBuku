from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core import serializers
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), 
                        content_type="application/json")

@login_required
def show_main_add_book(request):
    return render(request, 'book/add_book.html')


@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        isbn = request.POST.get("isbn")
        book_title = request.POST.get("book_title")
        book_author = request.POST.get("book_author")
        year_of_publication = request.POST.get("year_of_publication")
        publisher = request.POST.get("publisher")
        image_url_s = request.POST.get("image_url_s")
        user = request.user

        new_book = Book(isbn=isbn, book_title=book_title, book_author=book_author, year_of_publication=year_of_publication, publisher=publisher, image_url_s=image_url_s, user=user)
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()