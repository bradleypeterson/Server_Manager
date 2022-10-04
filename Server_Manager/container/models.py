from django.db import models

class Container(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created = models.DateField()
