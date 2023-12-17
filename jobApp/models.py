from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = [
        ('recruiter', 'Recruiter'),('jobseeker', 'JobSeeker')
    ]
    display_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_type = models.CharField(choices=USER, max_length=100)
    def __str__(self):
        return self.display_name
    

class JobModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField()
    job_image = models.ImageField(upload_to='media',  blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null= True)
    job_creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class CareerModel(models.Model):
    title = models.CharField(max_length=100)
    careerImage = models.ImageField(upload_to='media/career', blank=True, null=True)
    def __str__(self):
        return self.title