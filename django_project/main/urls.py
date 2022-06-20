from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path('dashboard', views.dashboard, name = "dashboard"),

    # urls for project
    path('dashboard/createproject', views.CreateProject.as_view(), name="create_project"),
    path('dashboard/list_projects', views.list_projects, name = "list_projects"),
    path('dashboard/project_detail/<int:id>/<slug:slug>/', views.project_detail, name="project_detail"),
    path('dashboard/edit_project/<int:pk>/', views.ProjectUpdateView.as_view(), name='edit_project'),
    # end urls for project

    # path('create-account/', views.createAccount, name = "Create Account"),
    #path('project/create/', views.createProject, name = "Create Project"),
    #path('objective/create/', views.createObjective, name = "Create Objective"),
    #path('metric/create/', views.createMetric, name = "Create Metric"),
]
