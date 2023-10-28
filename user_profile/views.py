from django.shortcuts import get_object_or_404, render
from user_profile.models import Profile
from django.contrib.auth.models import User
from main.views import register_request

# Create your views here.

def view_profile(request,username):
    user = get_object_or_404(User)  # Ambil berdasarkan username yang diberikan
    username = user.username
    context = {
        'user': username, 
    }

    return render(request, 'profile_page.html', context)

def update_user(request):
    return render(request, "update_user.html", {} )
    