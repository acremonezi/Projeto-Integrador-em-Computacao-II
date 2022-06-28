from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

