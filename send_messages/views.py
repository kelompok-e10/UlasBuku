from django.shortcuts import render
from django.contrib.auth.models import User
from send_messages.models import Messages
from send_messages.forms import MessagesForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

def show_messages(request):
    user = User.objects.filter(user=request.user)
    messages = Messages.objects.all()
    users = User.objects.all()

    context = {
        'user': user.username,
        'list_of_user': users,
        'list_of_messages': messages
    }

    return render(request, "messages.html", context)

def get_messages_by_id(request, user_id, contact_id):
    sent_messages = Messages.objects.filter(sender__id=user_id, recipient__id=contact_id)
    received_messages = Messages.objects.filter(sender__id=contact_id, recipient__id=user_id)
    context = {
        'sent_messages': sent_messages,
        'received_messages': received_messages
    }
    return render(request, "message.html", context)


def add_messages_by_ajax(request):
    if request.method == "POST":
        sender = request.POST.get("sender")
        recipient = request.POST.get("recipient")
        text = request.POST.get("text")
        timestamp = request.POST.get("timestamp")
        is_read = request.POST.get("is_read")
        
        new_messages = Messages(sender=sender, recipient=recipient, text=text, timestamp=timestamp, is_read=is_read)
        new_messages.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def create_text_messages(request):
    form = MessagesForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()

    context = {'form': form}
    return render(request, "message.html", context)


# Create your views here.
