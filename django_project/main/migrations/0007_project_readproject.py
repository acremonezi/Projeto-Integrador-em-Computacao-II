# Generated by Django 4.0.3 on 2022-06-20 13:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_project_editproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='readproject',
            field=models.ManyToManyField(blank=True, related_name='readproject', to=settings.AUTH_USER_MODEL),
        ),
    ]
