from django.db import models
from django.contrib.auth.models import User

# Table "Account"
class Account(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    accountName = models.CharField(max_length = 100)
    
    # User Owner Column
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)
 

# Table "Project"
class Project(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    projectName = models.CharField(max_length = 200)
    
    # User Owner Column
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Relationships
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    

# Table "Objective"
class Objective(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    objectiveName = models.CharField(max_length = 200)
    
    # Featured Columns
    targetValue = models.FloatField()
    targetUnit = models.CharField(max_length=3)
    targetDate = models.DateField()
    
    # User Owner Column
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Relationships
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


# Table "Metric"
class Metric(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    metricName = models.CharField(max_length = 200)
    
    # Featured Columns
    targetValue = models.FloatField()
    targetUnit = models.CharField(max_length=3)
    targetDate = models.DateField()
    
    # User Owner Column
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Relationships
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
