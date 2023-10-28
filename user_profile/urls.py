from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('<str:username>/', views.view_profile, name='view_profile'),
    path('<str:username>/add_description/', views.add_description, name='add_description'),
    path('<str:username>/get_description/', views.get_description, name='get_description'),
]