from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        display_name = request.POST.get('display_name')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = CustomUser.objects.create_user(username = username, display_name = display_name, email=email, user_type = user_type, password=password)
        user.save()
        return redirect('loginPage')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type == 'recruiter':
            teacher = {'names': ['mehedi', 'hasan', 'sami', 'ali']}
            context = {
                'myUser': 'Hi I am a Recruiter',
                'teacher': teacher
            }
            return render(request, 'recruiter/dashboard.html', context)
        elif user.user_type =='jobseeker':
            context = {
                'myUser': 'Hi I am a Jobseeker'
            }
            return render(request, 'jobseeker/dashboard.html', context)
        else:
            return HttpResponse('Invalid User')

    else:
        return HttpResponse('User is not Authenticated')




# {% if user.is_authenticated %}
#     logout
#     register
# {% else %}