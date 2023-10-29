from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.get_books, name='get_books'),
    path('show_main_add_book/', views.show_main_add_book, name='show_main_add_book'),
    path('add_book_ajax/', views.add_book_ajax, name='add_book_ajax'),
]