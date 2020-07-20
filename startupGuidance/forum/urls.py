from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('send_message', views.send_message, name='send_message'),
]
