#from re import A
from django.contrib import admin
from . import models

# Register your models here.

# Simple Method
#admin.site.register(models.Account)
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated', 'userOwner']
    list_filter = ['created', 'title']


admin.site.register(models.Objective)
admin.site.register(models.Metric)
