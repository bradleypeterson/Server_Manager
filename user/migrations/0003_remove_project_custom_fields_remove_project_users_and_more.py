# Generated by Django 5.1.7 on 2025-03-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_remove_group_project_group_projects'),
        ('project', '0001_initial'),
        ('user', '0002_customfield_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='custom_fields',
        ),
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='role',
        ),
        migrations.AddField(
            model_name='appuser',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='app_users', to='project.project'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='app_users', to='group.group'),
        ),
        migrations.DeleteModel(
            name='CustomField',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
