from html import entities
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('course', views.course, name='course'),
    path('tpologin',views.tpologin,name='tpologin'),
    path('entities',views.entities,name='entities')
    
]