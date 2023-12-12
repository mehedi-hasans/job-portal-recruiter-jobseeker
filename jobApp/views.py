from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# Create your views here.

def signupPage(request):
    
    return render(request, 'signup.html')

def loginPage(request):
    return render(request, 'login.html')

def logoutPage(request):
    return redirect('loginPage')

def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type == 'recruiter':
            return render(request, 'recruiter/dashboard.html')
        elif user.user_type =='jobseeker':
            return render(request, 'jobseeker/dashboard.html')
        else:
            return HttpResponse('Invalid User')

    else:
        return HttpResponse('User is not Authenticated')


