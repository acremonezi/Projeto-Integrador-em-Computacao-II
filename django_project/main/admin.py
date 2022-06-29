from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated', 'userOwner', 'active']
    list_filter = ['created', 'title']


@admin.register(models.Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated', 'project', 'active']
    list_filter = ['created', 'title']


@admin.register(models.Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated', 'objective', 'active']
    list_filter = ['created', 'title']

