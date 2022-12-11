from django.db import models

from courses.models import Course



# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=200)
    groupDescription = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class TestUser(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
