from django.db import models
from user.models import Project
from servermanager import settings

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100, unique=True)
    project_name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True, null=True)
    project = models.ManyToManyField(Project, related_name='project')

    def __str__(self):
        return self.group_name