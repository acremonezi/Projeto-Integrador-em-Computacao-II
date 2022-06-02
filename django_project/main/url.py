from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # path('create-account/', views.createAccount, name = "Create Account"),
    path('main', views.main, name = "Main"),
    path('project/create/', views.createProject, name = "Create Project"),
    path('objective/create/', views.createObjective, name = "Create Objective"),
    path('metric/create/', views.createMetric, name = "Create Metric"),
]