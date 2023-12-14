from django.urls import path
from . import views

urlpatterns = [
    path('', views.signupPage, name='signupPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutPage, name='logoutPage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view', views.viewJob, name='viewJob')
]