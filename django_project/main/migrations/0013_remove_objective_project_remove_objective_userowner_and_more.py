# Generated by Django 4.0.4 on 2022-06-29 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_status_project_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objective',
            name='project',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='userOwner',
        ),
        migrations.DeleteModel(
            name='Metric',
        ),
        migrations.DeleteModel(
            name='Objective',
        ),
    ]
