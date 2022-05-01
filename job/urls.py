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
    path('applyform/<int:job_id>', views.applyform, name='applyform'),
    path('check_application_valid/<int:job_id>/<int:user_id>', views.check_application_valid, name='check_application_valid'),
    path('apply/<int:job_id>/<int:user_id>', views.apply, name="apply"),
    path('studentapply', views.studentapply, name='studentapply'),
    path('applyinternform/<int:intern_id>', views.applyinternform, name='applyinternform'),
    path('applyintern/<int:intern_id>/<int:user_id>', views.applyintern, name="applyintern"),

]