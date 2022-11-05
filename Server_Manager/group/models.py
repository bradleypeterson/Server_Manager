from django.db import models


# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=200)
    groupDescription = models.TextField(null=True)
    groupCredentials = models.CharField(max_length=200)
