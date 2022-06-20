from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Project(models.Model):
    # Main Columns
    title = models.CharField('Titulo', max_length = 200)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    slug = models.SlugField(max_length=200, blank=True)
    # User Owner Column
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_owner')
    # Permissions
    editproject = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='editproject', blank=True)
    readproject = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='readproject', blank=True)

    def get_absolute_url(self):  # for get one project
        return reverse('main:project_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):  # for slug
        if not self.slug:
            self.slug = slugify(f'{self.userOwner}-{self.title}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name: 'Projeto'
        verbose_name_plural: 'Projetos'


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

# Table "Account"
# OBS: It will be maybe used in the future for multi-tenancy accounts.

# class Account(models.Model):
#     # Main Columns
#     createdDate = models.DateField(auto_now_add=True)
#     accountName = models.CharField(max_length = 100)

#     # User Owner Column
#     userOwner = models.ForeignKey(User, on_delete=models.CASCADE)


# Table "Project"