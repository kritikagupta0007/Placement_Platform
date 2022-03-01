from django.contrib import admin

# Register your models here.
from .models import JobForm, PlacementDetail, InternshipForm, Applied, AppliedIntern

admin.site.register(JobForm)
admin.site.register(PlacementDetail)
admin.site.register(InternshipForm)
admin.site.register(Applied)
admin.site.register(AppliedIntern)