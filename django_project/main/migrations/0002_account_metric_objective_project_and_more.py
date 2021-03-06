from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('accountName', models.CharField(max_length=100)),
                ('userOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('metricName', models.CharField(max_length=200)),
                ('targetValue', models.FloatField()),
                ('targetUnit', models.CharField(max_length=3)),
                ('targetDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('objectiveName', models.CharField(max_length=200)),
                ('targetValue', models.FloatField()),
                ('targetUnit', models.CharField(max_length=3)),
                ('targetDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('projectName', models.CharField(max_length=200)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
                ('userOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='objectives',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='account',
        ),
        migrations.RemoveField(
            model_name='results',
            name='objective',
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
        migrations.DeleteModel(
            name='Objectives',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.AddField(
            model_name='objective',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project'),
        ),
        migrations.AddField(
            model_name='objective',
            name='userOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='metric',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.objective'),
        ),
        migrations.AddField(
            model_name='metric',
            name='userOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
