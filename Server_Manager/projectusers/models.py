from django.db import models

class ProjectUser(models.Model):
    projectid = models.IntegerField()
    userid = models.IntegerField()
    accesslevel = models.IntegerField()
    accessgranteddate = models.DateField()
    accessupdateddate = models.DateField()
    accessgranteduserid = models.IntegerField()

