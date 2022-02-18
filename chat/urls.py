from django.urls import include, path

from . import views

urlpatterns = [
    path('run_alexa', views.run_alexa, name='run_alexa'),
   
]