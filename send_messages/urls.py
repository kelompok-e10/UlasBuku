from django.urls import path
from send_messages.views import show_messages, create_text_messages, user_messages_by_id

app_name = 'send_messages'

urlpatterns = [
    path('', show_messages, name='show_messages'),
    path('create_text_messages/', create_text_messages, name='create_text_messages'),
    path('user_messages_by_id/<int:contact_id>/', user_messages_by_id, name='user_messages_by_id'),
]