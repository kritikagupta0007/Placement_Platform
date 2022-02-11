from django.contrib import admin

# Register your models here.
from .models import JobForm, PlacementDetail

admin.site.register(JobForm)
admin.site.register(PlacementDetail)