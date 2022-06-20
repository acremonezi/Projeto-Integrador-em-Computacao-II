#from re import A
from django.contrib import admin
from . import models

# Register your models here.

# Simple Method
#admin.site.register(models.Account)
admin.site.register(models.Project)
admin.site.register(models.Objective)
admin.site.register(models.Metric)
