from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from send_messages.models import Messages
from send_messages.forms import MessagesForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q, Max
from django.template import loader
from main import*
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="main:login")
def show_messages(request):
    users = User.objects.order_by("username")
    template = loader.get_template("pesan/index.html")

    context = {
        'user': request.user,
        'username': request.user.username,
        'list_of_user': users,
    }

    return HttpResponse(template.render(context, request))

@login_required(login_url="main:login")
def user_messages_by_id(request, selected_user_id):
    selected_user = User.objects.get(id=selected_user_id)
    form = MessagesForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        text = form.save(commit=False)
        text.sender = request.user
        text.recipient = selected_user
        text.save()
        return redirect("send_messages:user_messages_by_id", selected_user_id)
    
    users = User.objects.order_by("username")
    messages = Messages.objects.filter(Q(sender=request.user.id, recipient=selected_user_id) | Q(
               sender=selected_user_id, recipient=request.user.id)).order_by("timestamp")
    template = loader.get_template("pesan/messages.html")
    context = {
        'list_of_user': users,
        'selected_user_id': selected_user_id,
        'selected_user': selected_user,
        'messages': messages,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="main:login")
def send(request, recipient_id):
    sender_id = request.user.id

def get_json(request):
    data = Messages.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def user_info_for_flutter(request, username):
    if request.method == 'GET':
        # Temukan pengguna saat ini
        current_user = User.objects.get(username=username)

        # Temukan semua pengguna lain yang berkomunikasi dengan pengguna saat ini
        other_users = User.objects.exclude(id = current_user.id).order_by('username')

        # Inisialisasi dictionary untuk menyimpan last message dari setiap user
        data = {}

        # Loop melalui setiap pengguna lain
        for other_user in other_users:
            # Ambil pesan terakhir antara pengguna saat ini dan pengguna lain
            last_message = Messages.objects.filter(
                Q(sender=current_user, recipient=other_user) | Q(
                    sender=other_user, recipient=current_user)
            ).order_by('-timestamp').first()
            # other_username = User.objects.get(id=other_user).username
            if last_message is not None:
                data[other_user.username] = {
                    'fields': {
                        'user id': current_user.id,
                        'selected user': other_user.username,
                        'selected user id': other_user.id,
                        'text': last_message.text
                    }
                }
            else:
                field = {
                    'fields': {
                        'user id': current_user.id,
                        'selected user': other_user.username,
                        'selected user id': other_user.id,
                        'text': 'Mulai percakapan'
                    }
                }
                data[other_user.username] = field
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def get_messages_flutter(request, current_user, selected_user):
    if request.method == 'GET':
        current_user_id = User.objects.get(username=current_user)
        selected_user_id = User.objects.get(username=selected_user)
        messages = Messages.objects.filter(Q(sender=current_user_id, recipient=selected_user_id) | Q(
                   sender=selected_user_id, recipient=current_user_id)).order_by("-timestamp")
        
        return HttpResponse(serializers.serialize("json", messages), content_type="application/json")

@csrf_exempt
def send_messages_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recipient = User.objects.get(id=int(data.get('recipient')))
        new_messages = Messages.objects.create(
            sender = request.user,
            recipient = recipient,
            text = data.get('text'),
        )  
        new_messages.save()
        return JsonResponse({'status': 'success'}, status = 200)
    else:
        return JsonResponse({'status': 'error'}, status = 401)


 