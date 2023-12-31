from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('<str:username>/', views.view_profile, name='view_profile'),
    path('<str:username>/add_description/', views.add_description, name='add_description'),
    path('<str:username>/edit_profile/', views.edit_profile, name='edit_profile'),
    path('<str:username>/get_json/', views.get_json, name='get_json'),
    path('<str:username>/update_profile_flutter/', views.update_profile_flutter, name='update_profile_flutter')
]