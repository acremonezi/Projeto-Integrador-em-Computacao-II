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
    active = models.BooleanField(default=True)

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


class Objective(models.Model):
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_owner_objective')
    title = models.CharField('Titulo', max_length = 200)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    slug = models.SlugField(max_length=200, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='objective_for_project')
    can_edit_objective = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='can_edit_objective', blank=True)
    can_read_objective = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='can_read_objective', blank=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):  # for get one project
        return reverse('main:objective_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):  # for slug
        if not self.slug:
            self.slug = slugify(f'{self.project}-{self.title}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name: 'Objetivo'
        verbose_name_plural: 'Objetivos'


class Metric(models.Model):
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_owner_metric')
    title = models.CharField('Titulo', max_length = 200)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)
    slug = models.SlugField(max_length=200, blank=True)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='metric_for_objective')
    can_edit_metric = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='can_edit_metric', blank=True)
    can_read_metric = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='can_read_metric', blank=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):  # for get one metric
        return reverse('main:metric_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):  # for slug
        if not self.slug:
            self.slug = slugify(f'{self.objective}-{self.title}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name: 'Métrica'
        verbose_name_plural: 'Métricas'
