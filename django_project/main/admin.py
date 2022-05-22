from re import A
from django.contrib import admin
from main.models import Account, Project, Objective, Metric

# Register your models here.

# Simple Method
admin.site.register(Account)
admin.site.register(Project)
admin.site.register(Objective)
admin.site.register(Metric)