from django.contrib import admin
from .models import *
# Register your models here.
class Custom_User_Display(admin.ModelAdmin):
    list_display = ['display_name', 'email', 'user_type']


admin.site.register(CustomUser, Custom_User_Display)