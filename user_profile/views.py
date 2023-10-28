from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from user_profile.models import Profile
from django.contrib.auth.models import User
from main.views import login_request, register_request
from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }

    return render(request, 'profile_page.html', context)

@login_required
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

@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')

        # Simpan data profil yang diperbarui
        user.profile.first_name = first_name
        user.profile.last_name = last_name
        user.profile.email = email
        user.profile.contact = contact
        user.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def get_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = user.profile  # Mendapatkan objek Profile yang sesuai dengan pengguna

    # Sekarang, Anda bisa mengakses atribut-atribut profil seperti first_name, last_name, email, contact_phone, dll.
    first_name = user_profile.first_name
    last_name = user_profile.last_name
    email = user_profile.email
    contact = user.profile.contact
    
    # Kemudian Anda dapat mengembalikan data profil dalam format JSON atau sejenisnya.
    profile_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'contact': contact,
    }

    return JsonResponse(profile_data)


    