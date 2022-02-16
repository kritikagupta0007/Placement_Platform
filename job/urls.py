from django.urls import include, path

from . import views

urlpatterns = [
    path('tpohome',views.tpohome,name='tpohome'),
    path('logout', views.logout, name='logout'),
    path('tporole', views.tporole, name='tporole'),
    path('addjob', views.addjob, name='addjob'),
    path('viewjob', views.viewjob, name='viewjob'),
    path('adddetails', views.adddetails,name='adddetails' ),
    path('placementdetails', views.placementdetails,name='placementdetails' ),
    path('addinternship', views.addinternship, name='addinternship'),
    path('internshipdetails', views.internshipdetails, name='internshipdetails'),
    path('description', views.description, name='description'),

]