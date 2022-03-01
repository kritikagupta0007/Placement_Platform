from django.urls import include, path

from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('run_alexa', views.start_chat, name='run_alexa'),
   
]