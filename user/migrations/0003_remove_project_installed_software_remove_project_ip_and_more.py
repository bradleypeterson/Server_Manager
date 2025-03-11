# Generated by Django 5.1.5 on 2025-03-07 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customfield_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='installed_software',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='project',
            name='issues',
        ),
        migrations.RemoveField(
            model_name='project',
            name='os',
        ),
        migrations.RemoveField(
            model_name='project',
            name='purpose',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tech_stack',
        ),
        migrations.AddField(
            model_name='project',
            name='currently_in_use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='github_repo_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='last_audit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='stack',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='trello_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='user_rights',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('operating_system', models.CharField(max_length=100)),
                ('ip_address', models.GenericIPAddressField()),
                ('software_installed', models.TextField(blank=True, null=True)),
                ('idrac_info', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('custom_fields', models.ManyToManyField(to='user.customfield')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='server_projects', to='user.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='servers',
            field=models.ManyToManyField(related_name='projects', to='user.server'),
        ),
    ]
