from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.get_books, name='get_books'),
]