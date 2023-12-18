import json
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import logout
import datetime

from forum_discussion.models import Header
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
    return render(request, "main/home.html")

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:homepage")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {"user":request.user}
    return render(request, "main/login.html", context)

def register_request(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, "main/register.html", context)

def logout_request(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:homepage")) 
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def create_discussion_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_thread = Header.objects.create(
            user = request.user,
            book_title = data["bookTitle"],
            rating = int(data["rating"]),
            review = data["review"]
        )

        new_thread.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)