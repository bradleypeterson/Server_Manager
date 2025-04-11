# Generated by Django 5.1.7 on 2025-04-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_remove_group_projects'),
        ('project', '0009_project_updated_by_server_updated_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='project',
            field=models.ManyToManyField(related_name='groups_project', to='project.project'),
        ),
    ]
