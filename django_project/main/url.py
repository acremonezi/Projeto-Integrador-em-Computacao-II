from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('create-account/', views.createAccount, name = "Create Account"),
    path('create-project/', views.createProject, name = "Create Project"),
    path('create-objective/', views.createObjective, name = "Create Objective"),
    path('create-metric/', views.createMetric, name = "Create Metric"),
]