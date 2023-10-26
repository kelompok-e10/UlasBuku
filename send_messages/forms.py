from django.forms import ModelForm
from send_messages.models import Messages

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["sender", "recipient", "text", "is_read"]
