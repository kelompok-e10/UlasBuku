from django.urls import path
from send_messages.views import show_messages, user_messages_by_id

app_name = 'send_messages'

urlpatterns = [
    path('', show_messages, name='show_messages'),
    path('user_messages_by_id/<int:selected_user_id>', user_messages_by_id, name='user_messages_by_id'),
] 