from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated', 'userOwner']
    list_filter = ['created', 'title']


admin.site.register(models.Objective)
admin.site.register(models.Metric)
# admin.site.register(models.Account)
