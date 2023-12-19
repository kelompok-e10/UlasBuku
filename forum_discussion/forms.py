from django.forms import ModelForm
from forum_discussion.models import Header

class DiscussionForm(ModelForm):
    class Meta:
        model = Header
        fields = ["book_title", "rating", "review"]