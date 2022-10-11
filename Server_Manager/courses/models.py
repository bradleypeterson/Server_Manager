from django.db import models

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=200)
