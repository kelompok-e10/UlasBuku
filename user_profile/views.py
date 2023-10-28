from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from user_profile.models import Profile
from django.contrib.auth.models import User
from main.views import login_request, register_request
from django.contrib.auth.decorators import login_required

def view_profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }

    return render(request, 'profile_page.html', context)

def add_description(request, username):
    if request.method == 'POST':
        description = request.POST.get('description', '')

        # Simpan deskripsi ke profil pengguna
        user = get_object_or_404(User, username=username)
        user.profile.description = description
        user.profile.save()

        # Anda juga dapat memvalidasi data deskripsi di sini jika diperlukan

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_description(request, username):
    user = get_object_or_404(User, username=username)
    description = user.profile.description if user.profile.description else ""
    return JsonResponse({'description': description})


    