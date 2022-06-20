from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models

# Create an Account
# The reason it is necessary is just in case
# a user needs to have access to more than one Account/Organization.
# Image an Account as a "Company".

# def createAccount(request):
#     if request.method == 'GET':
#         return render(request, 'create-account/index.html')
    
#     elif request.method == 'POST':  
#         accountName = request.POST.get('accountName')
        
#         # Create an instance of the class "Account" named "account"
#         # and save it into the database.
#         account = Account(accountName = accountName)
#         account.save()
        
#         return HttpResponse('Conta Criada!')
        
        
# Create a Project
@login_required
def dashboard(request):
    projects = models.Project.objects.all().filter(userOwner=request.user.id)
    context = {'projects': projects}
    return render(request, 'main/dashboard.html', context)


class CreateProject(LoginRequiredMixin, CreateView):
    model = models.Project
    fields = ['title', 'editproject', 'readproject']
    extra_context = {'goal': 'Criar'}


@login_required
def list_projects(request):
    projects = models.Project.objects.filter(userOwner=request.user.id)
    context = {'projects': projects}
    return render(request, 'main/list_projects.html', context)


@login_required
def project_detail(request, id, slug):
    project = get_object_or_404(models.Project, id=id)
    context = {'project': project}
    return render(request, 'main/project_detail.html', context)


class PrecosUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectForm
    success_url = reverse_lazy('main:list_projects')
    extra_context = {'goal': 'Editar'}
'''    
def createProject(request):
    if request.method == 'GET':
        return render(request, 'create-project/index.html')
    
    elif request.method == 'POST':  
        projectName = request.POST.get('projectName')
        
        # The frontend need to provide a selection box showing
        # the "Accounts" in name of the user. So, the user can select one.
        
        # account = ...
        
        # Create an instance of the class "Project" named "project"
        # and save it into the database.
        project = Project(projectName = projectName)
        project.save()
        
        return HttpResponse('Projeto Criado!!')
    

# Create a Objective
def createObjective(request):
    if request.method == 'GET':
        return render(request, 'create-objective/index.html')
    
    elif request.method == 'POST':  
        objectiveName = request.POST.get('objectiveName')
        
        # The frontend need to provide a selection box showing
        # the "Projects" in name of the user. So, the user can select one.
        
        # project = ...
        
        # Create an instance of the class "Account" named "account"
        # and save it into the database.
        objective = Objective(objectiveName = objectiveName)
        objective.save()
        
        return HttpResponse('Objetivo Criado!')
    

# Create a Metric
def createMetric(request):
    if request.method == 'GET':
        return render(request, 'create-metric/index.html')
    
    elif request.method == 'POST':  
        metricName = request.POST.get('metricName')
        
        # The frontend need to provide a selection box showing
        # the "Objective" in name of the user. So, the user can select one.
        
        # objective = ....
        
        # Create an instance of the class "Metric" named "metric"
        # and save it into the database.
        metric = Metric(metricName = metricName)
        metric.save()
        
        return HttpResponse('Metrica Criada!')
'''