from django.db import models
from group.models import Group
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    ROLE = (
        ('faculty', 'faculty'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=100, choices=ROLE, default='faculty')

