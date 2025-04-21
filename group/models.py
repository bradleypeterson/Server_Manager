from django.db import models
from servermanager import settings

class Group(models.Model):
    #Group Models stored in SQLite
    group_name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_users', blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.group_name