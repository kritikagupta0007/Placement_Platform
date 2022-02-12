from django.urls import path

from . import views

urlpatterns = [
    path('tporole', views.tporole, name='tporole'),
    path('addjob', views.addjob, name='addjob'),
    path('viewjob', views.viewjob, name='viewjob'),
    path('adddetails', views.adddetails,name='adddetails' ),
    path('placementdetails', views.placementdetails,name='placementdetails' ),
    path('addinternship', views.addinternship, name='addinternship'),
    path('internshipdetails', views.internshipdetails, name='internshipdetails'),

]