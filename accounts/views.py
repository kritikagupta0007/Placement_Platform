from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

# Create your views here.

def course(request):
    return render(request, 'courses.html')

def entities(request):
    return render(request,'entities.html')

def description(request):
    return render(request,'description.html')


def register(request):

    if request.method == "POST":
        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['password1']
        psw2 = request.POST['password2']
        # university_roll_number = request.POST['university_roll_number']
        # admission_number = request.POST['admission_number']
        # name = request.POST['full_name']
        # father_name = request.POST['father_name']
        # mother_name = request.POST['mother_name']
        # aadhar_number = request.POST['aadhar_number']
        # dateOfBirth = request.POST['dateOfBirth']
        # gender = request.POST['gender']
        # marks1 = request.POST['marks1']
        # marks2 = request.POST['marks2']
        # marks3 = request.POST['marks3']
        # branch = request.POST['branch']
        # phone_number = request.POST['phone_number']
        # parents_number = request.POST['parents_number']
        # upload_resume = request.POST['upload_resume']

        
            # if Register.objects.filter(university_rollnumber = university_roll_number).exists():
            #    messages.info(request, 'University Roll Number exist')
            #    return redirect('register')
            # elif Register.objects.filter(admission_number = admission_number).exists():
            #     messages.info(request, 'Admission Number exist')
            #     return redirect('register')
            # elif Register.objects.filter(aadhar_number = aadhar_number).exists():
            #     messages.info(request, 'Aadhar Number exist')
            #     return redirect('register')
            # elif Register.objects.filter(phone_number = phone_number).exists():
            #     messages.info(request, 'Phone number exist')
            #     return redirect('register')
        if psw == psw2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username exist')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email exist')
                return redirect('register')
            else:
                # register = Register(university_rollnumber =  university_roll_number, admission_number=admission_number,full_name=name, email=email, father_name = father_name, password=psw,mother_name = mother_name, aadhar_number =  aadhar_number, date_Of_Birth = dateOfBirth, gender=gender, class_10th_percentage = marks1,class_12th_percentage = marks2,btech_percentage = marks3,  btech_branch = branch ,phone_number = phone_number,parents_phone_number = parents_number, upload_Resume =  upload_resume)
                user = User.objects.create_user(first_name = first_name, last_name = last_name,username = username, email = email, password = psw )
                user.save()
                print("user created")
                print(user.email)
                print(user.password)
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')

    else:
        return render(request, 'register.html')



def login(request):

    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        
        user = auth.authenticate(username=u, password=p)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/') 
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def tpologin(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']

        user = auth.authenticate(username=u, password=p)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('tpohome') 
        
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('tpologin')
    
    else:
        return render(request, 'tpologin.html')
