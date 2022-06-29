from django import forms
from . import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'editproject', 'readproject', 'active']


class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = models.Objective
        fields = ['title', 'project', 'can_edit_objective', 'can_read_objective', 'active']


class MetricForm(forms.ModelForm):
    class Meta:
        model = models.Metric
        fields = ['title', 'objective', 'can_edit_metric', 'can_read_metric', 'active']
