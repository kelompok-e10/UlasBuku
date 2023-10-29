from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Forum

def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    my_forums = Forum.objects.filter(author=user)

    context = {
        'user': user,
        'my_forums': my_forums,
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

def get_json(request, username):
    user = get_object_or_404(User, username=username)
    description = user.profile.description if user.profile.description else ""
    profile_data = {
        'first_name': user.profile.first_name,
        'last_name': user.profile.last_name,
        'email': user.email,
        'contact': user.profile.contact,
    }
    return JsonResponse({'description': description,
                         'profile_data':profile_data})

@login_required
def edit_profile(request, username):
    if request.method == 'POST':
        # Ambil nilai-nilai yang dikirim melalui POST
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')

        # Simpan perubahan ke profil pengguna
        user = get_object_or_404(User, username=username)
        user.profile.first_name = first_name
        user.profile.last_name = last_name
        user.profile.email = email
        user.profile.contact = contact
        user.profile.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

