from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path('dashboard', views.dashboard, name = "dashboard"),
    # path('create-account/', views.createAccount, name = "Create Account"),
    #path('project/create/', views.createProject, name = "Create Project"),
    #path('objective/create/', views.createObjective, name = "Create Objective"),
    #path('metric/create/', views.createMetric, name = "Create Metric"),
]
