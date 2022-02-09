from django.db import models

# Create your models here.

class JobForm(models.Model):
    company = models.CharField(max_length=50, default='', editable=True)
    profile = models.CharField(max_length=30, default='', editable=True)
    package = models.IntegerField(default = 0)
    eligibility = models.CharField(max_length=100, default='', editable=True)
    drive_date = models.CharField(max_length=15, default='', editable=True)
    last_date = models.CharField(max_length=15, default='', editable=True)
    status = models.CharField(max_length=15, default='', editable=True)