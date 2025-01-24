from django.db import models
from user.models import AppUser
from group.models import TestUser

class Project(models.Model):
    project_title = models.CharField(max_length=50)
    project_description = models.TextField()
    docker_id = models.CharField(max_length=50)
    project_language = models.CharField(max_length=50)
    project_database = models.CharField(max_length=50)
    project_backend = models.CharField(max_length=50)
    project_technology_misc = models.CharField(max_length=50)
    project_link = models.CharField(max_length=50)
    project_image_link = models.CharField(max_length=50)
    added_date = models.DateField()
    updated_date = models.DateField()
    user = models.ForeignKey(TestUser, on_delete=models.CASCADE)
