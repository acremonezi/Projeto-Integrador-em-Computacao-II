# Generated by Django 4.0.4 on 2022-06-19 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_project_createddate_project_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='projectName',
            new_name='title',
        ),
    ]
