from django.forms import ModelForm
from send_messages.models import Messages
from django.forms import Textarea

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["text"]
        widgets={
        'text': Textarea(attrs={'rows': 1, 'cols': 0}),
        }
