# Generated by Django 5.1.7 on 2025-03-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_initial'),
        ('project', '0003_project_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='projects',
            field=models.ManyToManyField(related_name='group_projects', to='project.project'),
        ),
    ]
