from django.urls import path
from send_messages.views import show_messages, create_text_messages, add_messages_by_ajax, get_messages_by_id

app_name = 'send_messages'

urlpatterns = [
    path('', show_messages, name='show_messages'),
    path('create_text_messages', create_text_messages, name='create_text_messages'),
    path('add_messages_by_ajax', add_messages_by_ajax, name='add_messages_by_ajax'),
    path('get_messages_by_id', get_messages_by_id, name='get_messages_by_id')
]