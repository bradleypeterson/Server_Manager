from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
    groups = models.ManyToManyField("group.Group", blank=True, related_name='app_users')
    projects = models.ManyToManyField("project.Project", blank=True, related_name='app_users')
