from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('<str:username>/', views.view_profile, name='view_profile')
]