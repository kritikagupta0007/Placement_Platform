from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    aadhar_number = models.IntegerField(max_length=10)