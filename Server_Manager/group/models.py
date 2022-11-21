from django.db import models

from courses.models import Course



# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=200)
    groupDescription = models.TextField(null=True)
    groupCredentials = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)