import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import re

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def register(request):
    # print("ASUU")
    data = json.loads(request.body)
    print(data);
    username = data.get('username')
    password = data.get('password')
    password_confirmation = data.get('password_confirmation')
 
    # # Password validation
    # if len(password) < 8:
    #     return JsonResponse({
    #         "status": False,
    #         "message": "Registrasi gagal, password harus paling sedikit 8 karakter."
    #     }, status=400)
    # elif not re.search("[A-Z]", password):
    #     return JsonResponse({
    #         "status": False,
    #         "message": "Registrasi gagal, password harus memiliki setidaknya satu huruf kapital."
    #     }, status=400)
    # elif not re.search("[0-9]", password):
    #     return JsonResponse({
    #         "status": False,
    #         "message": "Registrasi gagal, password harus memiliki setidaknya satu angka."
    #     }, status=400)
    # elif password != password_confirmation:
    #     return JsonResponse({
    #         "status": False,
    #         "message": "Registrasi gagal, password dan password tidak sesuai."
    #     }, status=400)
    
    # Username validation
    # if User.objects.filter(username=username).exists():
    #     return JsonResponse({
    #         "status": False,
    #         "message": "Registrasi gagal, username telah digunakan."
    #     }, status=400)
        
    # Create user
    if (User.objects.create_user(username=username, email=username, password=password) != None):
        user = User.objects.create_user(username=username, email=username, password=password)
        user.save()
        return JsonResponse({
            "username": user.username,
            "status": True,
            "message": "Registrasi berhasil! User dengan nama {username} berhasil dibuat."
        }, status=200)
        
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil. Sampai jumpa {username}!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout gagal."
        }, status=401)