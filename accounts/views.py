from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def course(request):
    return render(request, 'courses.html')


def register(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        psw = request.POST['psw']
        psw2 = request.POST['psw2']

        if psw == psw2:
            if User.objects.filter(username = username).exists():
               messages.info(request, 'Username exist')
               return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email exist')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=name, email=email, username = username, password=psw)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')

    else:
        return render(request, 'register.html')



def login(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
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