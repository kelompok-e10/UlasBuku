from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from user_profile.models import Profile
from django.contrib.auth.models import User
from main.views import register_request

# Create your views here.
def view_profile(request):
    user = get_object_or_404(User),

    context = {
        'name' : user.username,
        'description' : user.description
    }

    return render(request, 'profile_page.html', context)

def update_user(request):
    return render(request, "update_user.html", {} )
    