import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import re
from django.db import IntegrityError
from django.contrib.auth.backends import UserModel


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
    data = json.loads(request.body)
    username = data.get('username')
    password1 = data.get('password')
    password_confirmation = data.get('password_confirmation')
    print(username)
    print(data)

    if UserModel.objects.filter(username=username).exists():
        return JsonResponse({"status": "duplicate"}, status=401)

    if password1 != password_confirmation:
        return JsonResponse({"status": "pass failed"}, status=401)
    
    createUser = User.objects.create_user(
        username = username, 
        password = password1,
    )
    print(createUser)
    createUser.save()
    return JsonResponse({
            "username": username,
            "status": "success",
            "message": f"Registrasi berhasil! User dengan nama {username} berhasil dibuat."
    }, status=200)
    # try:
    #     user = User.objects.create_user(username=username, email=username, password=password)
    #     user.save()
    #     return JsonResponse({
    #         "username": user.username,
    #         "status": True,
    #         "message": f"Registrasi berhasil! User dengan nama {username} berhasil dibuat."
    #     }, status=200)
    # except IntegrityError:
    #     return JsonResponse({
    #         "status": False,
    #         "message": "Registrasi gagal, username telah digunakan."
    #     }, status=400)
        
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