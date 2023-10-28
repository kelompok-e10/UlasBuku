from django.urls import path
from user_profile.views import view_profile

app_name = 'user_profile'

urlpatterns = [
    path('', view_profile, name='view_profile'),
]