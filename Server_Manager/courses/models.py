from django.db import models



# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=200)
    courseDescription = models.TextField(null=True)
    courseStudentCount = models.IntegerField()
    courseGroups = models.CharField(max_length=100)
