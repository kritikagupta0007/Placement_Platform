import datetime
from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    university_rollnumber = models.IntegerField(default = 0)
    admission_number = models.CharField(max_length=9, default='', editable=True)
    full_name = models.CharField(max_length=30,default='', editable=True)
    father_name = models.CharField(max_length=30, default='', editable=True)
    mother_name = models.CharField(max_length=30, default='', editable=True)
    aadhar_number = models.IntegerField(default = 0)
    date_Of_Birth = models.DateField(("Date"), default=datetime.date.today)
    gender = models.CharField(max_length=6, default='', editable=True)
    class_10th_percentage = models.IntegerField(default = 0)
    class_12th_percentage = models.IntegerField(default = 0)
    btech_percentage = models.IntegerField(default = 0)
    btech_branch = models.CharField(max_length=6, default='', editable=True)
    phone_number = models.IntegerField(default = 0)
    parents_phone_number = models.IntegerField(default=0)
    upload_Resume = models.FileField(upload_to=None, default= '',max_length=254)
    email = models.EmailField(max_length=30, default='', editable=True)
    password = models.CharField(max_length=30, default='', editable=True)


