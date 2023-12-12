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
    confirm_password = models.CharField(max_length=100)
    user_type = models.CharField(choices=USER, max_length=100)
    def __str__(self):
        return self.display_name
    