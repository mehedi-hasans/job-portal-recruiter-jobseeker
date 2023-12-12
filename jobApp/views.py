from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
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


