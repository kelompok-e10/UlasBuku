from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
<<<<<<< HEAD
    path('register/', register, name='register'),
=======
>>>>>>> e2fff03a5225263b5bc000460da424bc52c4bfa7
    path('logout/', logout, name='logout'),
]