from django.contrib import admin
from .models import CustomUser, JobModel, CareerModel

class CustomUserDisplay(admin.ModelAdmin):
    list_display = ['display_name', 'email', 'user_type']

admin.site.register(CustomUser, CustomUserDisplay)
admin.site.register(JobModel)
admin.site.register(CareerModel)