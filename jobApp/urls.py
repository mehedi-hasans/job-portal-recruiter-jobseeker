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
    path('deletePage/<str:myid>', views.deletePage, name='deletePage'),
    path('editPage/<str:myid>', views.editPage, name='editPage'),
    path('updatePage', views.updatePage, name='updatePage'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)