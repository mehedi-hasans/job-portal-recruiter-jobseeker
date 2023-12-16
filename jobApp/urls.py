from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.signupPage, name='signupPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutPage, name='logoutPage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view', views.viewJob, name='viewJob'),
    path('addJob', views.addJob, name='addJob'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)