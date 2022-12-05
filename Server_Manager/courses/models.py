from django.db import models
from user.models import AppUser



# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=200)
    courseDescription = models.TextField(null=True)
    courseStudentCount = models.IntegerField()
    courseGroups = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)