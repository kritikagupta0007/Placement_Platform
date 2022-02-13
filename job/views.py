from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from job.models import JobForm, PlacementDetail, InternshipForm
from django.contrib.auth.models import auth

# Create your views here.

def tporole(request):
    return render(request, 'tporole.html')

def tpohome(request):
    return render(request, 'tpohome.html')

def addjob(request):
    if request.method == 'POST':
        cname = request.POST.get("companyname")
        profile = request.POST.get("profile")
        package = request.POST.get("package")
        eligible = request.POST.get("eligible")
        drive_date = request.POST.get("date")
        last_date = request.POST.get("lastDate")
        link = request.POST.get("link")
        add = JobForm(company=cname, profile=profile, package=package, eligibility=eligible, drive_date=drive_date, last_date=last_date, link_to_apply=link)
        add.save()
        return redirect("tporole")

    else:
        return render(request, 'addjob.html')


def viewjob(request):
    addjob = JobForm.objects.all()
    print(addjob)
    data = {
        'addjob' : addjob
    }

    return render(request, 'job.html', data)



def adddetails(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        upload = request.POST.get("upload_resume")
        add = PlacementDetail(title=title, description=desc, upload_file=upload )
        add.save()
        return redirect("tporole")
    
    else:
        return render(request, 'add_details.html')


def placementdetails(request):
    placement = PlacementDetail.objects.all()
    print(placement)
    data = {
        'placement' : placement
    }

    return render(request, 'placement_details.html', data)


def addinternship(request):
    if request.method == 'POST':
        cname = request.POST.get("companyname")
        profile = request.POST.get("profile")
        skills = request.POST.get("skills")
        stipend = request.POST.get("stipend")
        duration = request.POST.get("duration")
        last_date = request.POST.get("lastDate")
        link = request.POST.get("link")
        add = InternshipForm(company=cname, profile=profile, skills=skills, stipend=stipend, duration=duration, last_date=last_date, link_to_apply=link)
        add.save()
        return redirect("tporole")

    else:
        return render(request, 'add_internship.html')

def internshipdetails(request):
    internship = InternshipForm.objects.all()
    print(internship)
    data = {
        'internship' : internship
    }

    return render(request, 'internship_details.html', data)


def logout(request):
    auth.logout(request)
    return redirect('/')