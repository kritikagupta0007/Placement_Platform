from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from job.models import JobForm

# Create your views here.

def tporole(request):
    return render(request, 'tporole.html')

def addjob(request):
    if request.method == 'POST':
        cname = request.POST.get("companyname")
        profile = request.POST.get("profile")
        package = request.POST.get("package")
        eligible = request.POST.get("eligible")
        drive_date = request.POST.get("date")
        last_date = request.POST.get("lastDate")
        status = request.POST.get("status")
        add = JobForm(company=cname, profile=profile, package=package, eligibility=eligible, drive_date=drive_date, last_date=last_date, status=status)
        add.save()
        return redirect("tporole")

    else:
        return render(request, 'addjob.html')
