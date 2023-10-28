from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from send_messages.models import Messages
from send_messages.forms import MessagesForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.template import loader

@login_required
def show_messages(request):
    users = User.objects.order_by("username")
    template = loader.get_template("pesan/index.html")

    context = {
        'user': request.user,
        'username': request.user.username,
        'list_of_user': users,
    }

    return HttpResponse(template.render(context, request))

@login_required
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

@login_required
def send(request, recipient_id):
    sender_id = request.user.id
