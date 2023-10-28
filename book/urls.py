from django.urls import path
from book import views

app_name = 'book'
urlpatterns = [
    path('', views.get_book, name='get_book'),
]