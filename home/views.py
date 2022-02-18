from turtle import home
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import views as auth_views


# Create your views here.

urlPatterns = [('forgotpass/', auth_views.PasswordChangeView.as_view(template_name='forgotpass.html'),),]

def index(request):
    #Variable
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

@permission_required('home.login', raise_exception=True)
@login_required
def login(request):
    if request.method == "POST":
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        User = authenticate(request, Username=Username, Password=Password)
        if User is not None:
            login(request, User)
            messages.error(request,"you are logdin")
            return redirect('index')
        else: 
            messages.error(request,"Invalid login") 
            return redirect('login') 
        # login.save()
    else:
        return render(request, 'login.html')
    
    if not request.User.is_authenticated:
        return render(request,'login_error.html')
    

def logout(request):
    logout(request)
    return HttpResponseRedirect('/index')

def Registration(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username Already Teken")
            if User.objects.filter(email = email).exists():
                messages.error(request,"Email Already Taken")
            else:
                user = User.objects.create(username = username, first_name = fname, last_name = lname, email = email, password = pass1)
                user.save()
                if user is not None:
                    auth.login(request,user)
                    return HttpResponse("Register Successfully and Logged In")

        else:
            messages.error(request,"Both Password are not matched")
    else:
        return render(request, 'Registration.html')
    Registration.save()

def appointment(request):
    return render(request, 'appointment.html')
    #return HttpResponse("This is appointment form page")

def treatment(request):
    messages.success(request,'')
    return render(request,'treatment.html')
    treatment.save()
    #return HttpResponse("This is user profile from page")

def events(request):
    messages.success(request,' ')
    return render(request,'events.html')
    events.save()
    #return HttpResponse("This is user profile from page")

def health(request):
    messages.success(request, ' ')
    return render(request, 'health.html')
    #return HttpResponse("This is user profile form page")

def forgotpass(request):
    return render(request, 'forgotpass.html')
    return HttpResponse("This is user profile form page")
