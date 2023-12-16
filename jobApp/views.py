from django.shortcuts import redirect, render
from django.http import HttpResponse

from jobApp.forms import JobCreateForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

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
        jobView = JobModel.objects.all()
        career = CareerModel.objects.all()
        context = {
            'jobs': jobView,
            'career': career,
        }
        return render(request, 'dashboard.html', context)

@login_required
def viewJob(request):
    jobView = JobModel.objects.all()
    return render(request, 'viewjob.html', {'jobs':jobView})




# def is_recruiter(user):
#     return user.groups.filter(name='addJob').exists()

@login_required
# @user_passes_test(is_recruiter)
def addJob(request):
    form = JobCreateForm()
    user = request.user
    if user.is_authenticated:
        if user.user_type == 'recruiter':
            return render(request, 'recruiter/addJob.html', {'form': form})
    else:
         return HttpResponse('User is not authenticate')
    return HttpResponse('User is not recruiter')

# {% if user.is_authenticated %}
#     logout
#     register
# {% else %}