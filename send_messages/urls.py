from django.urls import path
from send_messages.views import *

app_name = 'send_messages'

urlpatterns = [
    path('', show_messages, name='show_messages'),
    path('user_messages_by_id/<int:selected_user_id>/', user_messages_by_id, name='user_messages_by_id'),
    path('json/', get_json, name='get_json'), 
    path('user_info/<str:username>/', user_info_for_flutter, name='user_info_for_flutter'),
    path('message_list/<str:current_user>/<str:selected_user>/', get_messages_flutter, name='message_list'),
    path('send/', send_messages_flutter, name='send_messages_flutter'),
]