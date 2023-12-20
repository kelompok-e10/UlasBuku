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

def show_main_add_book(request):
    return render(request, 'book/add_book.html')

def show_json_by_id(request, id):
    data = Book.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", data), 
                        content_type="application/json")