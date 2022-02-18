from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class JobForm(models.Model):
    company = models.CharField(max_length=50, default='', editable=True)
    profile = models.CharField(max_length=30, default='', editable=True)
    package = models.IntegerField(default = 0)
    eligibility = models.CharField(max_length=100, default='', editable=True)
    drive_date = models.CharField(max_length=15, default='', editable=True)
    last_date = models.CharField(max_length=15, default='', editable=True)
    link_to_apply = models.URLField(max_length = 200, default='', editable=True)

    def __str__(self):
        return self.company


class PlacementDetail(models.Model):
    title = models.CharField(max_length=50, default='', editable=True)
    description = models.CharField(max_length=500, default='', editable=True)
    upload_file = models.FileField(upload_to=None, default= '',max_length=254) # excel file holding names and details of selected students


class InternshipForm(models.Model):
    company = models.CharField(max_length=50, default='', editable=True)
    profile = models.CharField(max_length=30, default='', editable=True)
    skills = models.CharField(max_length=50, default='', editable=True)
    stipend = models.IntegerField(default = 0)
    duration = models.CharField(max_length=15, default='', editable=True)
    last_date = models.CharField(max_length=15, default='', editable=True)
    link_to_apply = models.URLField(max_length = 200, default='', editable=True)
    

class Applied(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(JobForm, on_delete=models.CASCADE)
    resume = models.FileField(upload_to=None, default='' ,max_length=254)
    is_selected = models.BooleanField(default=False)

