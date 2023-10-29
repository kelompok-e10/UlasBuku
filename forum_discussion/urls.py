from django.urls import path
from . import views

app_name = 'forum_discussion'

urlpatterns = [
    path('', views.view_forum, name='view_forum'),
    path('get_header_json/', views.get_header_json, name='get_header_json'),
    path('add/', views.add_discussion_ajax, name='add_discussion_ajax'),
    path('reply/', views.add_reply_ajax, name='add_reply_ajax'),
    path('delete/<int:id>/', views.delete_discussion, name='delete_discussion'),
]