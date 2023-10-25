from django.urls import path
from main.views import *
from book.views import *

app_name = 'book'

urlpatterns = [
    path("", get_books, name="get_books"),
]