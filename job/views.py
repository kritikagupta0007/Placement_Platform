from django import views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import HttpResponse
from job.models import AppliedIntern, JobForm, PlacementDetail, InternshipForm, Applied
from django.contrib.auth.models import User, auth

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
    jobs = JobForm.objects.all().order_by('-id')
    data = []
    for job in jobs:
        applied = list(Applied.objects.filter(job_id=job))
        data.append(
            {
                'id': job.id,
                'company' : job.company,
                'profile': job.profile,
                'package' : job.package,
                'eligibility' : job.eligibility,
                'drive_date' : job.drive_date,
                'last_date' : job.last_date,
                'applied_count' : len(applied)
            }
        )    
    print(job)
    return render(request, 'job.html', {'jobs': data})



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
    placement = PlacementDetail.objects.all().order_by('-id')
    print(placement)
    data = {
        'placement' : placement
    }

    return render(request, 'placement_details.html', data)
    


def description(request):
    placement = PlacementDetail.objects.all()
    print(placement)
    data = {
        'placement' : placement
    }

    return render(request, 'description.html', data)



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
    internship = InternshipForm.objects.all().order_by('-id')
    data = []
    for intern in internship:
        applied = list(AppliedIntern.objects.filter(intern_id=intern))
        data.append(
            {
                'id': intern.id,
                'company' : intern.company,
                'profile': intern.profile,
                'package' : intern.skills,
                'eligibility' : intern.stipend,
                'drive_date' : intern.duration,
                'last_date' : intern.last_date,
                'applied_count' : len(applied)
            }
        )    
    print(data)
    return render(request, 'internship_details.html', {'internship' :data})



def logout(request):
    auth.logout(request)
    return redirect('/')


def applyform(request, job_id):
    job_id = job_id
    return render(request, 'applied.html', {'job_id':job_id})


def apply(request, job_id, user_id):

    if request.method == 'POST':
        job_id = job_id   #job id from url
        user_id =user_id  #user id from url
        print(job_id)
        print(user_id)
        resume_link = request.POST['resume']
        job = JobForm.objects.get(id=job_id)
        user = User.objects.get(id=user_id)
        if Applied.objects.filter(user_id = user, job_id = job).exists():
            messages.info(request, 'You Already Applied for this Job')
            return redirect('viewjob')
        else:
            table =  Applied(user_id= user, job_id= job, resume=resume_link)
            table.save()
            return redirect('/')

def studentapply(request):
    student = Applied.objects.all().order_by('-job_id')
    print(student)
    data = {
        'student' : student
    }
    return render(request, 'student_applied.html', data)


def applyinternform(request, intern_id):
    intern_id = intern_id
    return render(request, 'applied_intern.html', {'intern_id':intern_id})


def applyintern(request, intern_id, user_id):

    if request.method == 'POST':
        intern_id = intern_id   #job id from url
        user_id =user_id  #user id from url
        print(intern_id)
        print(user_id)
        resume_link = request.POST['resume']
        intern = InternshipForm.objects.get(id=intern_id)
        user = User.objects.get(id=user_id)
        if AppliedIntern.objects.filter(user_id = user, intern_id = intern).exists():
            messages.info(request, 'You Already Applied for this Job')
            return redirect('internshipdetails')
        else:
            table =  AppliedIntern(user_id= user, intern_id= intern, resume=resume_link)
            table.save()
            return redirect('/')

def check_application_valid(request, job_id, user_id):
    job = JobForm.objects.get(id=job_id)
    user = User.objects.get(id=user_id)
    if Applied.objects.filter(user_id = user, job_id = job).exists():
        messages.info(request, 'You Already Applied for this Job')
        return redirect('viewjob')
    else:
        return render(request, 'applied.html', {'job_id':job_id})
# 2 views1. form _OpenTextWritingModefor submit

# jobs = [
#     {id=1, profile, companyname, date},
#     {id=2},
#     {id=3}
# ]

# applied = [
#     {job=1, user=3, resume=""},
#     {job=1, user=67, resume=""},
#     {job=2, user=45, resume=""}
# ]

# applied_data_count = {
#     1: 2,
#     2: 1,
#     3: 0
# }