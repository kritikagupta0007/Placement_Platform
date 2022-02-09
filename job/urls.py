from django.urls import path

from . import views

urlpatterns = [
    path('tporole', views.tporole, name='tporole'),
    path('addjob', views.addjob, name='addjob'),
]