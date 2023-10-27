from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import User_profile

# Create your views here.
def view_profile(request, username):
    user = get_object_or_404(User_profile, user__username=username),

    context = {
        'name' : user,
        'age' : user.age,
        'description' : user.description,
    }

    return render(request, 'profile_page.html', context)
    