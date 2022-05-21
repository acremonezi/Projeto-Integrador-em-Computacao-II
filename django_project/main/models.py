from django.db import models

# The relationship between the django-allauth
# user tables and the "Accounts" table bellow was not
# done yet to avoid mistakes.

# Table "Accounts"
class Accounts(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length = 200)

# Table "Projects"
class Projects(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length = 200)
    
    # Relationships
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    

# Table "Objectives"
class Objectives(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length = 200)
    
    # Featured Columns
    targetValue = models.FloatField()
    targetUnit = models.CharField(max_length=3)
    targetDate = models.DateField()

    # Relationships
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)


# Table "results"
class Results(models.Model):
    # Main Columns
    createdDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length = 200)
    
    # Featured Columns
    targetValue = models.FloatField()
    targetUnit = models.CharField(max_length=3)
    targetDate = models.DateField()
    
    # Relationships
    objective = models.ForeignKey(Objectives, on_delete=models.CASCADE)
