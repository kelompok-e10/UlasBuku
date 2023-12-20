from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.get_books, name='get_books'),
    path('show_main_add_book/', views.show_main_add_book, name='show_main_add_book'),
    path('<int:id>/', views.show_json_by_id, name='show_json_by_id'),
]