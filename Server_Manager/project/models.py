from django.db import models
from user.models import AppUser

class Project(models.Model):
    projecttitle = models.CharField(max_length=50)
    projectdescription = models.TextField()
    dockerid = models.CharField(max_length=50)
    projectlanguage = models.CharField(max_length=50)
    projectdatabase = models.CharField(max_length=50)
    projectbackend = models.CharField(max_length=50)
    projecttechnologymisc = models.CharField(max_length=50)
    projectlink = models.CharField(max_length=50)
    projectimagelink = models.CharField(max_length=50)
    addeddate = models.DateField()
    updateddate = models.DateField()
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)